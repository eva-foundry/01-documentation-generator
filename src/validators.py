"""
Validation functions for EVA Foundation documentation
"""

import re
import yaml
from typing import Dict, List


def validate_yaml_frontmatter(content: str) -> Dict:
    """Validate YAML front matter against schema"""
    try:
        if not content.strip().startswith("---"):
            return {"valid": False, "error": "Missing YAML front matter"}
        
        # Extract YAML
        yaml_match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
        if not yaml_match:
            return {"valid": False, "error": "Malformed YAML front matter"}
        
        yaml_content = yaml.safe_load(yaml_match.group(1))
        
        # Validate required fields
        required = ["document_type", "phase", "audience", "traceability"]
        for field in required:
            if field not in yaml_content:
                return {"valid": False, "error": f"Missing required field: {field}"}
        
        # Validate types
        if not isinstance(yaml_content["audience"], list):
            return {"valid": False, "error": "audience must be a list"}
        
        if not isinstance(yaml_content["traceability"], list):
            return {"valid": False, "error": "traceability must be a list"}
        
        return {"valid": True}
    except yaml.YAMLError as e:
        return {"valid": False, "error": f"YAML parse error: {e}"}
    except Exception as e:
        return {"valid": False, "error": str(e)}


def validate_yaml_values(content: str) -> Dict:
    """Validate YAML field values against standards"""
    try:
        match = re.search(r'^---\n(.+?)\n---', content, re.DOTALL | re.MULTILINE)
        if not match:
            return {"valid": False, "error": "No YAML frontmatter found"}
        
        frontmatter = yaml.safe_load(match.group(1))
        errors = []
        
        # Validate document_type
        valid_types = ["architecture", "technical_design", "operational", "governance", "conops"]
        if "document_type" in frontmatter:
            if frontmatter["document_type"] not in valid_types:
                errors.append(f"document_type must be one of {valid_types}")
        
        # Validate phase range
        if "phase" in frontmatter:
            phase = frontmatter["phase"]
            if not isinstance(phase, int) or not ((0 <= phase <= 7) or phase == 99):
                errors.append("phase must be integer 0-7 or 99")
        
        # Validate audience format (should be list)
        if "audience" in frontmatter:
            if not isinstance(frontmatter["audience"], list):
                errors.append("audience must be multi-line list format (not inline)")
        
        # Validate traceability format (allow with or without #ID, validate anchor format)
        if "traceability" in frontmatter:
            if not isinstance(frontmatter["traceability"], list):
                errors.append("traceability must be list format")
            else:
                for trace in frontmatter["traceability"]:
                    # Accept formats: source-materials/requirements-v0.2/FILE.md or FILE.md#ID or FILE.md#Section-Name
                    if '#' in trace:
                        # Validate format with anchor: FILE.md#ID or FILE.md#Section-Name
                        # Examples: #INF01, #IT01-DA (requirement IDs) or #Backup-&-Recovery, #Testing-Strategy (section names)
                        if not re.search(r'source-materials/requirements-v0\.2/.+\.md#[A-Za-z0-9\-&]+$', trace):
                            errors.append(f"traceability entry '{trace}' with anchor must follow format: source-materials/requirements-v0.2/FILE.md#ID or FILE.md#Section-Name (e.g., #INF01, #IT01-DA, #Backup-&-Recovery)")
                            break
                    else:
                        # Validate format without anchor: FILE.md only
                        if not re.search(r'source-materials/requirements-v0\.2/.+\.md$', trace):
                            errors.append(f"traceability entry '{trace}' must follow format: source-materials/requirements-v0.2/FILE.md")
                            break
        
        if errors:
            return {"valid": False, "errors": errors}
        return {"valid": True}
    except Exception as e:
        return {"valid": False, "error": str(e)}


def validate_consumability(content: str) -> Dict:
    """Check AI-consumability requirements"""
    errors = []
    warnings = []
    
    # Check for tables
    if "|" not in content or not re.search(r"\|.*\|.*\|", content):
        warnings.append("No markdown tables found - consider using tables for comparisons")
    
    # Check for code blocks
    if "```" not in content:
        warnings.append("No code blocks found")
    
    # Check for code blocks without language tags
    untagged_blocks = re.findall(r"```\n", content)
    if untagged_blocks:
        warnings.append(f"Found {len(untagged_blocks)} code blocks without language tags")
    
    # Check for ambiguous pronouns
    ambiguous_patterns = [
        r"\b(it|this|that)\s+(is|was|will|should|must)\b",
        r"\bthey\s+(are|were|will)\b"
    ]
    ambiguous_count = 0
    for pattern in ambiguous_patterns:
        ambiguous_count += len(re.findall(pattern, content, re.IGNORECASE))
    
    if ambiguous_count > 10:  # Threshold
        warnings.append(f"Excessive ambiguous pronouns: {ambiguous_count} instances")
    
    # Check for "see above" references
    see_above_pattern = r"\b(see above|as mentioned|as discussed|as stated earlier)\b"
    if re.search(see_above_pattern, content, re.IGNORECASE):
        errors.append("Found 'see above' or similar - use explicit markdown links")
    
    # Check for file references without links
    file_refs = re.findall(r"`[\w\-/]+\.(?:py|md|ts|tsx|json|yaml|yml)`", content)
    if file_refs:
        # Check if they're wrapped in markdown links
        for ref in file_refs[:5]:  # Check first 5
            if ref not in content or f"]({ref[1:-1]})" not in content:
                warnings.append(f"File reference without link: {ref}")
                break
    
    return {"errors": errors, "warnings": warnings}


def validate_traceability(content: str) -> Dict:
    """Validate requirement traceability to v0.2 sources"""
    
    # Check for requirement IDs (INF01, ACC03, IOP01, etc.)
    req_pattern = r"\b[A-Z]{2,3}\d{2}\b"
    req_ids = re.findall(req_pattern, content)
    
    if len(req_ids) == 0:
        return {
            "valid": False,
            "error": "No v0.2 requirement IDs found (expected format: INF01, ACC03, etc.)"
        }
    
    # Check for source-materials file references (accept both old and new formats)
    if "src-v02/" not in content and "source-materials/requirements-v0.2/" not in content:
        return {
            "valid": False,
            "error": "No references to source files (expected src-v02/ or source-materials/requirements-v0.2/)"
        }
    
    # Check for traceability section
    if "traceability" not in content.lower() and "implementation evidence" not in content.lower():
        return {
            "valid": False,
            "error": "Missing traceability or implementation evidence section"
        }
    
    return {"valid": True, "requirement_ids": len(req_ids)}


def validate_required_sections(content: str, phase: int) -> Dict:
    """Validate required sections are present"""
    errors = []
    
    # Extract phase from content if not provided
    if phase is None:
        match = re.search(r'^---\n(.+?)\n---', content, re.DOTALL | re.MULTILINE)
        if match:
            try:
                frontmatter = yaml.safe_load(match.group(1))
                phase = frontmatter.get("phase", 1)
            except:
                phase = 1
        else:
            phase = 1
    
    # Required sections for all phase 1+ documents
    if phase >= 1:
        required = [
            (r'##\s*\d*\.?\s*In Scope', "In Scope section"),
            (r'##\s*\d*\.?\s*Out of Scope', "Out of Scope section"),
            (r'##\s*\d*\.?\s*(Primary|Core|Target|Key)\s*(Audience|Users|Actors|Stakeholders)', "Primary Audience/Users/Actors section"),
            (r'##\s*\d*\.?\s*Implementation Evidence', "Implementation Evidence section")
        ]
        
        for pattern, name in required:
            if not re.search(pattern, content, re.IGNORECASE):
                errors.append(f"Missing required section: {name}")
    
    # Check section numbering consistency (only if ALL sections are numbered)
    all_sections = re.findall(r'^##\s+', content, re.MULTILINE)
    numbered_sections = re.findall(r'^##\s*(\d+)\.', content, re.MULTILINE)
    if numbered_sections and len(numbered_sections) == len(all_sections):
        # If ALL sections are numbered, enforce consecutive numbering
        nums = [int(n) for n in numbered_sections]
        expected = list(range(1, len(nums) + 1))
        if nums != expected:
            errors.append(f"Section numbering not consecutive: found {nums}, expected {expected}")
    
    if errors:
        return {"valid": False, "errors": errors}
    return {"valid": True}


def validate_phase_content(phase: int, content: str) -> Dict:
    """Validate content specific to each phase"""
    errors = []
    
    phase_requirements = {
        0: ["overview", "architecture", "glossary"],
        1: ["infrastructure", "deployment", "azure"],
        2: ["backend", "frontend", "api"],
        3: ["feature", "capability", "workflow"],
        4: ["monitoring", "logging", "observability"],
        5: ["security", "compliance", "authentication"],
        6: ["testing", "validation", "quality"],
        7: ["development", "contribution", "setup"]
    }
    
    required_terms = phase_requirements.get(phase, [])
    content_lower = content.lower()
    
    missing_terms = [term for term in required_terms if term not in content_lower]
    if missing_terms:
        errors.append(f"Phase {phase} content missing expected terms: {', '.join(missing_terms)}")
    
    return {"valid": len(errors) == 0, "errors": errors}


def validate_file_completeness(content: str, expected_sections: List[str]) -> Dict:
    """Check if all required sections are present"""
    missing = []
    
    for section in expected_sections:
        # Check for section header (## or ###)
        pattern = rf"#{1,3}\s+{re.escape(section)}"
        if not re.search(pattern, content, re.IGNORECASE):
            missing.append(section)
    
    return {
        "valid": len(missing) == 0,
        "missing_sections": missing
    }


def validate_cross_references(content: str, available_files: List[str]) -> Dict:
    """Validate internal markdown links"""
    errors = []
    warnings = []
    
    # Find all markdown links [text](path)
    link_pattern = r"\[([^\]]+)\]\(([^\)]+)\)"
    links = re.findall(link_pattern, content)
    
    for text, path in links:
        # Skip external URLs
        if path.startswith("http://") or path.startswith("https://"):
            continue
        
        # Skip anchors within same doc
        if path.startswith("#"):
            continue
        
        # Extract file path (remove anchors)
        file_path = path.split("#")[0]
        
        # Check if referenced file exists in available files
        if file_path and file_path not in available_files:
            # Check if it's a relative reference
            if not file_path.startswith("../") and not file_path.startswith("./"):
                warnings.append(f"Reference to '{file_path}' (check relative path)")
            else:
                errors.append(f"Broken reference: '{file_path}'")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }


def validate_markdown_syntax(content: str) -> Dict:
    """Basic markdown syntax validation"""
    errors = []
    warnings = []
    
    # Check for unclosed code blocks
    code_block_count = content.count("```")
    if code_block_count % 2 != 0:
        errors.append("Unclosed code block (odd number of ```)")
    
    # Check for malformed tables
    table_lines = [line for line in content.split("\n") if line.strip().startswith("|")]
    if table_lines:
        # Check separator line exists
        has_separator = any(re.match(r"\|[\s\-:]+\|", line) for line in table_lines)
        if not has_separator:
            warnings.append("Table found but missing separator line")
    
    # Check for heading hierarchy (no skipping levels)
    heading_pattern = r"^(#{1,6})\s"
    headings = []
    for line in content.split("\n"):
        match = re.match(heading_pattern, line)
        if match:
            level = len(match.group(1))
            headings.append(level)
    
    for i in range(len(headings) - 1):
        if headings[i+1] > headings[i] + 1:
            warnings.append(f"Skipped heading level: {headings[i]} to {headings[i+1]}")
            break
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }


def validate_all_documents(output_dir: str) -> Dict:
    """Run all validations on generated documents"""
    import os
    from pathlib import Path
    
    results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "files": {}
    }
    
    output_path = Path(output_dir)
    if not output_path.exists():
        return {"error": f"Output directory not found: {output_dir}"}
    
    # Get all markdown files
    md_files = list(output_path.rglob("*.md"))
    available_files = [str(f.relative_to(output_path)) for f in md_files]
    
    for md_file in md_files:
        rel_path = str(md_file.relative_to(output_path))
        results["total"] += 1
        
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        file_results = {
            "frontmatter": validate_yaml_frontmatter(content),
            "consumability": validate_consumability(content),
            "traceability": validate_traceability(content),
            "markdown": validate_markdown_syntax(content),
            "cross_refs": validate_cross_references(content, available_files)
        }
        
        # Determine if file passed
        passed = all(
            result.get("valid", True) for result in file_results.values()
        )
        
        if passed:
            results["passed"] += 1
        else:
            results["failed"] += 1
        
        results["files"][rel_path] = file_results
    
    return results
