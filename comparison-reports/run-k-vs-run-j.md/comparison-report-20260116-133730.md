# Documentation Generator Comparison Report

**Generated:** 2026-01-16T13:37:30.017626
**Original Output:** `generated-output-run-j`
**New Output:** `generated-output`

## Executive Summary

**Overall Consistency Score:** 57.16%

- **Files Analyzed:** 25
- **Identical:** 0 (0.0%)
- **Similar:** 1 (4.0%)
- **Different:** 24 (96.0%)
- **Missing:** 3

## Production Readiness Assessment

❌ **NOT READY** - Generator lacks consistency (<70%)

## Per-File Comparison Matrix

| File | Overall Score | Structural | Content | Traceability | Issues |
|------|--------------|------------|---------|--------------|--------|
| 04-security-and-compliance\audit-and-logging.md | 82.3% | 100.0% | 64.6% | ✅ | Low content similarity: 0.65 |
| 01-architecture\physical-architecture.md | 79.1% | 100.0% | 58.2% | ✅ | Low content similarity: 0.58 |
| 01-architecture\network-topology.md | 74.2% | 94.4% | 51.6% | ✅ | Section structure differs; Low content similarity: 0.52 |
| 04-security-and-compliance\privacy-and-retention.md | 69.2% | 100.0% | 38.4% | ✅ | Low content similarity: 0.38 |
| 00-overview\scope-in-out.md | 66.5% | 100.0% | 32.9% | ✅ | Low content similarity: 0.33 |
| 05-operations-conops\backup-and-recovery.md | 65.8% | 75.0% | 46.6% | ✅ | YAML frontmatter differs; Low content similarity: 0.47 |
| 04-security-and-compliance\security-architecture.md | 64.7% | 75.0% | 44.5% | ✅ | YAML frontmatter differs; Low content similarity: 0.44 |
| 03-data-and-ai\data-ingestion-pipeline.md | 64.6% | 100.0% | 29.2% | ✅ | Low content similarity: 0.29 |
| 06-quality\accessibility.md | 64.0% | 100.0% | 67.9% | ❌ | Traceability references differ; Low content similarity: 0.68 |
| 00-overview\glossary-acronyms.md | 59.1% | 100.0% | 18.2% | ✅ | Low content similarity: 0.18 |
| 03-data-and-ai\prompt-and-config-governance.md | 58.5% | 75.0% | 32.0% | ✅ | YAML frontmatter differs; Low content similarity: 0.32 |
| 02-platform-components\eva-domain-assistant.md | 58.5% | 84.6% | 26.2% | ✅ | Section structure differs; Low content similarity: 0.26 |
| 04-security-and-compliance\rbac-model.md | 58.2% | 100.0% | 56.3% | ❌ | Traceability references differ; Low content similarity: 0.56 |
| 02-platform-components\eva-chat.md | 55.7% | 100.0% | 51.4% | ❌ | Traceability references differ; Low content similarity: 0.51 |
| 05-operations-conops\operating-model.md | 55.3% | 50.0% | 40.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.41 |
| 05-operations-conops\incident-and-contingency.md | 54.1% | 75.0% | 63.1% | ❌ | YAML frontmatter differs; Traceability references differ; Low content similarity: 0.63 |
| 02-platform-components\shared-foundation-services.md | 52.7% | 100.0% | 45.4% | ❌ | Traceability references differ; Low content similarity: 0.45 |
| 05-operations-conops\onboarding-offboarding.md | 52.6% | 50.0% | 35.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.35 |
| 03-data-and-ai\model-usage-and-guardrails.md | 50.6% | 52.3% | 29.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.30 |
| 01-architecture\system-context.md | 50.2% | 100.0% | 40.5% | ❌ | Traceability references differ; Low content similarity: 0.40 |
| 01-architecture\logical-architecture.md | 42.1% | 90.0% | 30.1% | ❌ | Section structure differs; Traceability references differ; Low content similarity: 0.30 |
| 03-data-and-ai\rag-patterns.md | 41.5% | 87.5% | 30.6% | ❌ | Section structure differs; Traceability references differ; Low content similarity: 0.31 |
| 00-overview\executive-summary.md | 39.7% | 65.0% | 40.4% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.40 |
| 06-quality\performance-and-scalability.md | 36.5% | 75.0% | 28.0% | ❌ | YAML frontmatter differs; Traceability references differ; Low content similarity: 0.28 |
| 05-operations-conops\change-and-release.md | 33.3% | 48.5% | 37.6% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.38 |
| 06-quality\testing-and-validation.md | N/A | N/A | N/A | N/A | File exists in only one output |
| 99-traceability\assumptions-risks-constraints.md | N/A | N/A | N/A | N/A | File exists in only one output |
| 99-traceability\requirements-mapping.md | N/A | N/A | N/A | N/A | File exists in only one output |

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