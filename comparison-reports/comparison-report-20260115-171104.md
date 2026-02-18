# Documentation Generator Comparison Report

**Generated:** 2026-01-15T17:11:04.833060
**Original Output:** `..\..\generated-output-backup-20260115-133611`
**New Output:** `..\..\generated-output`

## Executive Summary

**Overall Consistency Score:** 44.51%

- **Files Analyzed:** 28
- **Identical:** 0 (0.0%)
- **Similar:** 0 (0.0%)
- **Different:** 28 (100.0%)
- **Missing:** 0

## Production Readiness Assessment

❌ **NOT READY** - Generator lacks consistency (<70%)

## Per-File Comparison Matrix

| File | Overall Score | Structural | Content | Traceability | Issues |
|------|--------------|------------|---------|--------------|--------|
| 00-overview\executive-summary.md | 59.4% | 63.5% | 40.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.41 |
| 05-operations-conops\backup-and-recovery.md | 57.8% | 37.1% | 53.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.53 |
| 04-security-and-compliance\security-architecture.md | 55.2% | 91.7% | 15.3% | ✅ | Section structure differs; Low content similarity: 0.15 |
| 05-operations-conops\onboarding-offboarding.md | 54.8% | 73.0% | 25.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.26 |
| 02-platform-components\eva-domain-assistant.md | 54.4% | 72.6% | 25.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.25 |
| 99-traceability\requirements-mapping.md | 53.9% | 25.0% | 52.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.53 |
| 00-overview\scope-in-out.md | 50.3% | 25.0% | 45.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.46 |
| 02-platform-components\shared-foundation-services.md | 49.3% | 70.5% | 16.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.16 |
| 01-architecture\physical-architecture.md | 48.6% | 55.4% | 24.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.24 |
| 03-data-and-ai\model-usage-and-guardrails.md | 48.5% | 25.0% | 41.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.42 |
| 02-platform-components\eva-chat.md | 47.7% | 60.0% | 19.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.19 |
| 03-data-and-ai\rag-patterns.md | 47.5% | 40.0% | 30.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.31 |
| 00-overview\glossary-acronyms.md | 46.7% | 55.8% | 19.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 06-quality\performance-and-scalability.md | 46.3% | 25.0% | 37.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.38 |
| 99-traceability\assumptions-risks-constraints.md | 44.9% | 60.0% | 13.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.14 |
| 01-architecture\system-context.md | 44.6% | 25.0% | 34.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.34 |
| 06-quality\testing-and-validation.md | 42.3% | 36.1% | 22.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.23 |
| 01-architecture\logical-architecture.md | 42.3% | 25.0% | 29.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.30 |
| 03-data-and-ai\data-ingestion-pipeline.md | 41.2% | 50.0% | 12.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.12 |
| 04-security-and-compliance\audit-and-logging.md | 37.5% | 30.6% | 16.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.17 |
| 04-security-and-compliance\rbac-model.md | 37.4% | 25.0% | 19.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 03-data-and-ai\prompt-and-config-governance.md | 35.2% | 25.0% | 15.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.15 |
| 05-operations-conops\change-and-release.md | 34.9% | 25.0% | 14.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.15 |
| 05-operations-conops\operating-model.md | 34.3% | 25.0% | 13.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.14 |
| 06-quality\accessibility.md | 33.3% | 25.0% | 11.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.12 |
| 04-security-and-compliance\privacy-and-retention.md | 33.1% | 25.0% | 11.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.11 |
| 01-architecture\network-topology.md | 32.7% | 25.0% | 10.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.10 |
| 05-operations-conops\incident-and-contingency.md | 32.2% | 25.0% | 9.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.09 |

## Methodology

This comparison uses a multi-level semantic analysis:

1. **Structural Comparison (30% weight)**
   - YAML frontmatter consistency
   - Section header structure matching
   - Document organization validation

2. **Content Similarity (50% weight)**
   - Text-based semantic similarity using difflib SequenceMatcher
   - Character-level comparison after normalization
   - Threshold: ≥70% for acceptable similarity

3. **Traceability Validation (20% weight)**
   - Requirement reference consistency
   - Source material citation matching
   - Coverage delta analysis

**Overall Score Thresholds:**
- **Identical:** ≥95% similarity
- **Similar:** 80-95% similarity
- **Different:** <80% similarity

## Recommendations

- ⚠️  Review files with low similarity scores for potential issues
- ⚠️  Consider adjusting validation thresholds or prompts
- ⚠️  Manual review recommended before production use