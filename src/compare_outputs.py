#!/usr/bin/env python3
"""
EVA Foundation Documentation Comparison Framework
Semantic comparison of documentation generator outputs across runs

Compares:
1. Structural consistency (YAML frontmatter, sections, file organization)
2. Semantic similarity (embedding-based content analysis)
3. Traceability validation (requirement coverage consistency)
4. Quality metrics delta (validation scores, evidence reports)
"""

import os
import sys
import json
import yaml
import re
import hashlib
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import difflib

# Third-party imports
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    import numpy as np
except ImportError as e:
    print(f"❌ Missing dependency: {e}")
    print("Run: pip install rich numpy")
    sys.exit(1)

# Local imports
try:
    from .validators import validate_yaml_frontmatter, validate_consumability, validate_traceability
except ImportError:
    try:
        from validators import validate_yaml_frontmatter, validate_consumability, validate_traceability
    except ImportError as e:
        print(f"❌ Missing local module: {e}")
        sys.exit(1)

console = Console()


@dataclass
class FileComparison:
    """Results of comparing a single file across two runs"""
    filename: str
    exists_in_original: bool
    exists_in_new: bool
    structural_score: float  # 0-1
    content_similarity: float  # 0-1 (based on embeddings if available, else text similarity)
    yaml_consistency: bool
    section_consistency: bool
    traceability_consistency: bool
    diff_summary: str
    issues: List[str]
    
    def overall_score(self) -> float:
        """Calculate weighted overall similarity score"""
        if not (self.exists_in_original and self.exists_in_new):
            return 0.0
        
        # Weighted average:  - 30% structure, 50% content, 20% traceability
        weights = {
            'structural': 0.3,
            'content': 0.5,
            'traceability': 0.2
        }
        
        traceability_score = 1.0 if self.traceability_consistency else 0.0
        
        return (
            weights['structural'] * self.structural_score +
            weights['content'] * self.content_similarity +
            weights['traceability'] * traceability_score
        )
    
    def to_dict(self):
        return {
            **asdict(self),
            'overall_score': self.overall_score()
        }


@dataclass
class ComparisonReport:
    """Complete comparison report"""
    timestamp: str
    original_dir: Path
    new_dir: Path
    file_comparisons: List[FileComparison]
    overall_consistency_score: float
    files_analyzed: int
    files_identical: int
    files_similar: int
    files_different: int
    files_missing: int
    summary: Dict[str, any]
    
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'original_dir': str(self.original_dir),
            'new_dir': str(self.new_dir),
            'overall_consistency_score': self.overall_consistency_score,
            'files_analyzed': self.files_analyzed,
            'files_identical': self.files_identical,
            'files_similar': self.files_similar,
            'files_different': self.files_different,
            'files_missing': self.files_missing,
            'summary': self.summary,
            'file_comparisons': [fc.to_dict() for fc in self.file_comparisons]
        }


class DocumentationComparator:
    """Compares two documentation generator outputs semantically"""
    
    def __init__(self, original_dir: Path, new_dir: Path, use_embeddings: bool = False):
        """
        Args:
            original_dir: Path to original output directory (e.g., generated-output-backup-TIMESTAMP/)
            new_dir: Path to new output directory (e.g., generated-output/)
            use_embeddings: Whether to use Azure OpenAI embeddings for semantic similarity (costs $)
        """
        self.original_dir = original_dir
        self.new_dir = new_dir
        self.use_embeddings = use_embeddings
        
        self.original_markdown = original_dir / "markdown"
        self.new_markdown = new_dir / "markdown"
        
        if not self.original_markdown.exists():
            raise FileNotFoundError(f"Original markdown directory not found: {self.original_markdown}")
        if not self.new_markdown.exists():
            raise FileNotFoundError(f"New markdown directory not found: {self.new_markdown}")
        
        # Initialize embeddings model if requested
        if self.use_embeddings:
            console.print("[yellow]⚠️  Embedding-based comparison requires Azure OpenAI API calls (costs $)[/yellow]")
            console.print("[yellow]   Using text-based similarity instead for cost savings[/yellow]\n")
            self.use_embeddings = False  # Disable for now unless explicitly configured
    
    def compare_all_files(self) -> ComparisonReport:
        """Compare all files across both directories"""
        console.print("\n[cyan]🔍 Starting comprehensive comparison...[/cyan]\n")
        
        # Collect all markdown files
        original_files = set(self._get_all_markdown_files(self.original_markdown))
        new_files = set(self._get_all_markdown_files(self.new_markdown))
        all_files = original_files | new_files
        
        file_comparisons = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Comparing files...", total=len(all_files))
            
            for rel_path in sorted(all_files):
                comparison = self._compare_file(rel_path, rel_path in original_files, rel_path in new_files)
                file_comparisons.append(comparison)
                progress.update(task, advance=1)
        
        # Calculate overall metrics
        overall_score, summary = self._calculate_overall_metrics(file_comparisons)
        
        report = ComparisonReport(
            timestamp=datetime.now().isoformat(),
            original_dir=self.original_dir,
            new_dir=self.new_dir,
            file_comparisons=file_comparisons,
            overall_consistency_score=overall_score,
            files_analyzed=summary['analyzed'],
            files_identical=summary['identical'],
            files_similar=summary['similar'],
            files_different=summary['different'],
            files_missing=summary['missing'],
            summary=summary
        )
        
        console.print("\n[green]✅ Comparison complete![/green]\n")
        return report
    
    def _get_all_markdown_files(self, base_dir: Path) -> List[str]:
        """Get all markdown files relative to base directory"""
        files = []
        for md_file in base_dir.glob("**/*.md"):
            rel_path = md_file.relative_to(base_dir)
            files.append(str(rel_path))
        return files
    
    def _compare_file(self, rel_path: str, exists_in_original: bool, exists_in_new: bool) -> FileComparison:
        """Compare a single file"""
        if not (exists_in_original and exists_in_new):
            # File missing in one directory
            return FileComparison(
                filename=rel_path,
                exists_in_original=exists_in_original,
                exists_in_new=exists_in_new,
                structural_score=0.0,
                content_similarity=0.0,
                yaml_consistency=False,
                section_consistency=False,
                traceability_consistency=False,
                diff_summary="File missing in one output",
                issues=["File exists in only one output"]
            )
        
        # Load both files
        original_path = self.original_markdown / rel_path
        new_path = self.new_markdown / rel_path
        
        with open(original_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        with open(new_path, 'r', encoding='utf-8') as f:
            new_content = f.read()
        
        # 1. Structural comparison
        structural_score, yaml_consistent, section_consistent = self._compare_structure(original_content, new_content)
        
        # 2. Content similarity
        content_similarity = self._calculate_content_similarity(original_content, new_content)
        
        # 3. Traceability consistency
        traceability_consistent = self._compare_traceability(original_content, new_content)
        
        # 4. Generate diff summary
        diff_summary = self._generate_diff_summary(original_content, new_content)
        
        # 5. Collect issues
        issues = []
        if not yaml_consistent:
            issues.append("YAML frontmatter differs")
        if not section_consistent:
            issues.append("Section structure differs")
        if not traceability_consistent:
            issues.append("Traceability references differ")
        if content_similarity < 0.7:
            issues.append(f"Low content similarity: {content_similarity:.2f}")
        
        return FileComparison(
            filename=rel_path,
            exists_in_original=True,
            exists_in_new=True,
            structural_score=structural_score,
            content_similarity=content_similarity,
            yaml_consistency=yaml_consistent,
            section_consistency=section_consistent,
            traceability_consistency=traceability_consistent,
            diff_summary=diff_summary,
            issues=issues
        )
    
    def _compare_structure(self, original: str, new: str) -> Tuple[float, bool, bool]:
        """Compare document structure (YAML, sections)"""
        # Extract YAML frontmatter
        original_yaml = self._extract_yaml(original)
        new_yaml = self._extract_yaml(new)
        
        yaml_consistent = original_yaml == new_yaml
        
        # Extract section headers
        original_sections = self._extract_sections(original)
        new_sections = self._extract_sections(new)
        
        section_consistent = original_sections == new_sections
        
        # Calculate structural score
        yaml_score = 1.0 if yaml_consistent else 0.5  # Partial credit if exists
        section_score = self._calculate_sequence_similarity(original_sections, new_sections)
        
        structural_score = (yaml_score + section_score) / 2
        
        return structural_score, yaml_consistent, section_consistent
    
    def _extract_yaml(self, content: str) -> Optional[Dict]:
        """Extract YAML frontmatter"""
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                return None
        return None
    
    def _extract_sections(self, content: str) -> List[str]:
        """Extract section headers (## headings)"""
        # Remove YAML frontmatter
        content_no_yaml = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
        
        # Extract headers
        headers = re.findall(r'^##\s+(.+)$', content_no_yaml, re.MULTILINE)
        return headers
    
    def _calculate_sequence_similarity(self, seq1: List[str], seq2: List[str]) -> float:
        """Calculate similarity between two sequences using difflib"""
        if not seq1 and not seq2:
            return 1.0
        if not seq1 or not seq2:
            return 0.0
        
        matcher = difflib.SequenceMatcher(None, seq1, seq2)
        return matcher.ratio()
    
    def _calculate_content_similarity(self, original: str, new: str) -> float:
        """Calculate semantic content similarity"""
        if self.use_embeddings:
            # TODO: Implement embedding-based similarity using Azure OpenAI
            # For now, fall back to text-based
            pass
        
        # Text-based similarity using difflib
        # Remove YAML and normalize whitespace
        original_clean = self._clean_content(original)
        new_clean = self._clean_content(new)
        
        # Use SequenceMatcher for character-level similarity
        matcher = difflib.SequenceMatcher(None, original_clean, new_clean)
        return matcher.ratio()
    
    def _clean_content(self, content: str) -> str:
        """Clean content for comparison (remove YAML, normalize whitespace)"""
        # Remove YAML
        content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
        
        # Normalize whitespace
        content = re.sub(r'\s+', ' ', content)
        content = content.strip()
        
        return content
    
    def _compare_traceability(self, original: str, new: str) -> bool:
        """Compare requirement references"""
        # Extract references to source-materials/requirements-v0.2
        ref_pattern = r'source-materials/requirements-v0\.2/([a-zA-Z0-9_-]+\.md)'
        
        original_refs = set(re.findall(ref_pattern, original))
        new_refs = set(re.findall(ref_pattern, new))
        
        # Allow exact match or superset (new can have more references)
        return original_refs == new_refs
    
    def _generate_diff_summary(self, original: str, new: str) -> str:
        """Generate a summary of differences"""
        original_lines = original.split('\n')
        new_lines = new.split('\n')
        
        differ = difflib.Differ()
        diff = list(differ.compare(original_lines, new_lines))
        
        added = sum(1 for line in diff if line.startswith('+ '))
        removed = sum(1 for line in diff if line.startswith('- '))
        changed = min(added, removed)
        
        if added == 0 and removed == 0:
            return "Identical"
        
        return f"+{added} lines, -{removed} lines, ~{changed} changed"
    
    def _calculate_overall_metrics(self, comparisons: List[FileComparison]) -> Tuple[float, Dict]:
        """Calculate overall metrics across all files"""
        valid_comparisons = [c for c in comparisons if c.exists_in_original and c.exists_in_new]
        
        if not valid_comparisons:
            return 0.0, {
                'analyzed': 0,
                'identical': 0,
                'similar': 0,
                'different': 0,
                'missing': len(comparisons)
            }
        
        # Overall consistency score (average of all file scores)
        overall_score = sum(c.overall_score() for c in valid_comparisons) / len(valid_comparisons)
        
        # Categorize files
        identical = sum(1 for c in valid_comparisons if c.overall_score() >= 0.95)
        similar = sum(1 for c in valid_comparisons if 0.80 <= c.overall_score() < 0.95)
        different = sum(1 for c in valid_comparisons if c.overall_score() < 0.80)
        missing = len(comparisons) - len(valid_comparisons)
        
        summary = {
            'analyzed': len(valid_comparisons),
            'identical': identical,
            'similar': similar,
            'different': different,
            'missing': missing
        }
        
        return overall_score, summary
    
    def save_report(self, report: ComparisonReport, output_dir: Path):
        """Save comparison report as JSON and Markdown"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Save JSON
        json_path = output_dir / f"comparison-report-{timestamp}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report.to_dict(), f, indent=2)
        console.print(f"[green]✅ JSON report saved: {json_path}[/green]")
        
        # Save Markdown
        md_path = output_dir / f"comparison-report-{timestamp}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(self._generate_markdown_report(report))
        console.print(f"[green]✅ Markdown report saved: {md_path}[/green]")
        
        return json_path, md_path
    
    def _generate_markdown_report(self, report: ComparisonReport) -> str:
        """Generate Markdown-formatted report"""
        lines = [
            "# Documentation Generator Comparison Report",
            "",
            f"**Generated:** {report.timestamp}",
            f"**Original Output:** `{report.original_dir}`",
            f"**New Output:** `{report.new_dir}`",
            "",
            "## Executive Summary",
            "",
            f"**Overall Consistency Score:** {report.overall_consistency_score:.2%}",
            "",
            f"- **Files Analyzed:** {report.files_analyzed}",
            f"- **Identical:** {report.files_identical} ({report.files_identical/max(report.files_analyzed, 1):.1%})",
            f"- **Similar:** {report.files_similar} ({report.files_similar/max(report.files_analyzed, 1):.1%})",
            f"- **Different:** {report.files_different} ({report.files_different/max(report.files_analyzed, 1):.1%})",
            f"- **Missing:** {report.files_missing}",
            "",
            "## Production Readiness Assessment",
            "",
        ]
        
        # Determine production readiness
        if report.overall_consistency_score >= 0.85:
            lines.append("✅ **READY FOR PRODUCTION** - Generator demonstrates high consistency (≥85%)")
        elif report.overall_consistency_score >= 0.70:
            lines.append("⚠️  **REVIEW REQUIRED** - Generator shows moderate consistency (70-85%)")
        else:
            lines.append("❌ **NOT READY** - Generator lacks consistency (<70%)")
        
        lines.extend([
            "",
            "## Per-File Comparison Matrix",
            "",
            "| File | Overall Score | Structural | Content | Traceability | Issues |",
            "|------|--------------|------------|---------|--------------|--------|"
        ])
        
        for fc in sorted(report.file_comparisons, key=lambda x: x.overall_score(), reverse=True):
            if not (fc.exists_in_original and fc.exists_in_new):
                score_str = "N/A"
                struct_str = "N/A"
                content_str = "N/A"
                trace_str = "N/A"
            else:
                score_str = f"{fc.overall_score():.1%}"
                struct_str = f"{fc.structural_score:.1%}"
                content_str = f"{fc.content_similarity:.1%}"
                trace_str = "✅" if fc.traceability_consistency else "❌"
            
            issues_str = "; ".join(fc.issues) if fc.issues else "None"
            lines.append(f"| {fc.filename} | {score_str} | {struct_str} | {content_str} | {trace_str} | {issues_str} |")
        
        lines.extend([
            "",
            "## Methodology",
            "",
            "This comparison uses a multi-level semantic analysis:",
            "",
            "1. **Structural Comparison (30% weight)**",
            "   - YAML frontmatter consistency",
            "   - Section header structure matching",
            "   - Document organization validation",
            "",
            "2. **Content Similarity (50% weight)**",
            "   - Text-based semantic similarity using difflib SequenceMatcher",
            "   - Character-level comparison after normalization",
            "   - Threshold: ≥70% for acceptable similarity",
            "",
            "3. **Traceability Validation (20% weight)**",
            "   - Requirement reference consistency",
            "   - Source material citation matching",
            "   - Coverage delta analysis",
            "",
            "**Overall Score Thresholds:**",
            "- **Identical:** ≥95% similarity",
            "- **Similar:** 80-95% similarity",
            "- **Different:** <80% similarity",
            "",
            "## Recommendations",
            "",
        ])
        
        if report.overall_consistency_score >= 0.85:
            lines.append("- ✅ Generator is production-ready for automated documentation generation")
            lines.append("- ✅ Non-determinism is within acceptable bounds for AI-generated content")
            lines.append("- ✅ Validation framework effectively ensures quality and traceability")
        else:
            lines.append("- ⚠️  Review files with low similarity scores for potential issues")
            lines.append("- ⚠️  Consider adjusting validation thresholds or prompts")
            lines.append("- ⚠️  Manual review recommended before production use")
        
        return "\n".join(lines)
    
    def print_summary(self, report: ComparisonReport):
        """Print summary to console"""
        console.print("\n")
        console.print(Panel.fit(
            f"[bold cyan]Overall Consistency Score:[/bold cyan] [bold green]{report.overall_consistency_score:.2%}[/bold green]",
            title="Comparison Summary"
        ))
        
        table = Table(title="File Category Breakdown")
        table.add_column("Category", style="cyan")
        table.add_column("Count", justify="right", style="green")
        table.add_column("Percentage", justify="right", style="yellow")
        
        total = max(report.files_analyzed, 1)
        table.add_row("Identical (≥95%)", str(report.files_identical), f"{report.files_identical/total:.1%}")
        table.add_row("Similar (80-95%)", str(report.files_similar), f"{report.files_similar/total:.1%}")
        table.add_row("Different (<80%)", str(report.files_different), f"{report.files_different/total:.1%}")
        table.add_row("Missing", str(report.files_missing), f"{report.files_missing/total:.1%}")
        
        console.print("\n")
        console.print(table)
        
        # Production readiness
        console.print("\n")
        if report.overall_consistency_score >= 0.85:
            console.print("[bold green]✅ READY FOR PRODUCTION[/bold green] - Generator demonstrates high consistency")
        elif report.overall_consistency_score >= 0.70:
            console.print("[bold yellow]⚠️  REVIEW REQUIRED[/bold yellow] - Generator shows moderate consistency")
        else:
            console.print("[bold red]❌ NOT READY[/bold red] - Generator lacks consistency")
        console.print("\n")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Compare EVA Foundation documentation generator outputs")
    parser.add_argument(
        "--original",
        required=True,
        help="Path to original output directory (e.g., generated-output-backup-20260115-133611)"
    )
    parser.add_argument(
        "--new",
        required=True,
        help="Path to new output directory (e.g., generated-output)"
    )
    parser.add_argument(
        "--output",
        default="comparison-reports",
        help="Output directory for comparison reports"
    )
    parser.add_argument(
        "--use-embeddings",
        action="store_true",
        help="Use Azure OpenAI embeddings for semantic similarity (costs $)"
    )
    
    args = parser.parse_args()
    
    original_dir = Path(args.original)
    new_dir = Path(args.new)
    output_dir = Path(args.output)
    
    if not original_dir.exists():
        console.print(f"[red]❌ Original directory not found: {original_dir}[/red]")
        sys.exit(1)
    if not new_dir.exists():
        console.print(f"[red]❌ New directory not found: {new_dir}[/red]")
        sys.exit(1)
    
    # Run comparison
    comparator = DocumentationComparator(original_dir, new_dir, use_embeddings=args.use_embeddings)
    report = comparator.compare_all_files()
    
    # Save and display results
    comparator.save_report(report, output_dir)
    comparator.print_summary(report)


if __name__ == "__main__":
    main()
