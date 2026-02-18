# Documentation Generator Comparison Report

**Generated:** 2026-01-15T18:49:56.705462
**Original Output:** `..\..\generated-output-run-b`
**New Output:** `..\..\generated-output`

## Executive Summary

**Overall Consistency Score:** 42.36%

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
| 00-overview\scope-in-out.md | 57.3% | 65.0% | 35.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.36 |
| 05-operations-conops\onboarding-offboarding.md | 55.3% | 41.0% | 46.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.46 |
| 00-overview\executive-summary.md | 54.6% | 66.2% | 29.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.30 |
| 00-overview\glossary-acronyms.md | 54.2% | 75.0% | 23.5% | ✅ | YAML frontmatter differs; Low content similarity: 0.23 |
| 03-data-and-ai\data-ingestion-pipeline.md | 52.1% | 51.3% | 33.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.33 |
| 02-platform-components\eva-domain-assistant.md | 51.5% | 69.4% | 21.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.21 |
| 04-security-and-compliance\audit-and-logging.md | 51.2% | 25.0% | 47.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.47 |
| 03-data-and-ai\rag-patterns.md | 50.6% | 48.8% | 31.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.32 |
| 04-security-and-compliance\security-architecture.md | 48.5% | 62.5% | 19.5% | ✅ | Section structure differs; Low content similarity: 0.19 |
| 02-platform-components\eva-chat.md | 46.2% | 65.0% | 13.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.13 |
| 06-quality\testing-and-validation.md | 45.1% | 37.5% | 27.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.28 |
| 01-architecture\network-topology.md | 41.5% | 44.0% | 16.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.17 |
| 05-operations-conops\backup-and-recovery.md | 41.0% | 41.7% | 17.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.17 |
| 99-traceability\assumptions-risks-constraints.md | 39.5% | 37.5% | 16.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.16 |
| 01-architecture\system-context.md | 38.6% | 25.0% | 22.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.22 |
| 01-architecture\physical-architecture.md | 37.3% | 25.0% | 19.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 05-operations-conops\change-and-release.md | 36.7% | 25.0% | 18.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.18 |
| 04-security-and-compliance\privacy-and-retention.md | 36.6% | 25.0% | 18.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.18 |
| 05-operations-conops\operating-model.md | 36.6% | 37.0% | 11.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.11 |
| 03-data-and-ai\prompt-and-config-governance.md | 36.5% | 25.0% | 17.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.18 |
| 03-data-and-ai\model-usage-and-guardrails.md | 36.4% | 25.0% | 17.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.18 |
| 01-architecture\logical-architecture.md | 36.1% | 25.0% | 17.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.17 |
| 06-quality\performance-and-scalability.md | 35.3% | 38.6% | 7.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.07 |
| 02-platform-components\shared-foundation-services.md | 34.8% | 25.0% | 14.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.15 |
| 06-quality\accessibility.md | 34.0% | 25.0% | 13.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.13 |
| 05-operations-conops\incident-and-contingency.md | 33.5% | 25.0% | 12.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.12 |
| 99-traceability\requirements-mapping.md | 33.4% | 25.0% | 11.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.12 |
| 04-security-and-compliance\rbac-model.md | 31.7% | 25.0% | 8.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.08 |

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