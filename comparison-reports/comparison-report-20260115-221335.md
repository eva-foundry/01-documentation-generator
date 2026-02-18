# Documentation Generator Comparison Report

**Generated:** 2026-01-15T22:13:35.870855
**Original Output:** `..\..\generated-output-run-e`
**New Output:** `..\..\generated-output`

## Executive Summary

**Overall Consistency Score:** 42.40%

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
| 04-security-and-compliance\security-architecture.md | 63.3% | 75.0% | 41.6% | ✅ | YAML frontmatter differs; Low content similarity: 0.42 |
| 05-operations-conops\backup-and-recovery.md | 62.1% | 83.3% | 34.1% | ✅ | Section structure differs; Low content similarity: 0.34 |
| 03-data-and-ai\data-ingestion-pipeline.md | 58.2% | 55.8% | 42.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.43 |
| 03-data-and-ai\rag-patterns.md | 56.5% | 75.0% | 28.0% | ✅ | YAML frontmatter differs; Low content similarity: 0.28 |
| 05-operations-conops\onboarding-offboarding.md | 53.2% | 75.0% | 21.4% | ✅ | YAML frontmatter differs; Low content similarity: 0.21 |
| 03-data-and-ai\prompt-and-config-governance.md | 53.0% | 69.4% | 24.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.24 |
| 99-traceability\requirements-mapping.md | 51.9% | 61.4% | 27.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.27 |
| 01-architecture\physical-architecture.md | 50.9% | 66.7% | 21.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.22 |
| 05-operations-conops\change-and-release.md | 48.2% | 61.4% | 19.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 04-security-and-compliance\audit-and-logging.md | 45.0% | 100.0% | 29.9% | ❌ | Traceability references differ; Low content similarity: 0.30 |
| 00-overview\executive-summary.md | 44.8% | 50.0% | 19.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 00-overview\scope-in-out.md | 44.6% | 75.0% | 44.1% | ❌ | YAML frontmatter differs; Traceability references differ; Low content similarity: 0.44 |
| 05-operations-conops\incident-and-contingency.md | 43.7% | 69.4% | 45.8% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.46 |
| 00-overview\glossary-acronyms.md | 42.9% | 50.0% | 15.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.16 |
| 01-architecture\logical-architecture.md | 41.8% | 66.7% | 43.6% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.44 |
| 01-architecture\system-context.md | 41.0% | 67.9% | 41.2% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.41 |
| 06-quality\accessibility.md | 40.9% | 100.0% | 21.7% | ❌ | Traceability references differ; Low content similarity: 0.22 |
| 04-security-and-compliance\privacy-and-retention.md | 39.3% | 75.0% | 33.6% | ❌ | YAML frontmatter differs; Traceability references differ; Low content similarity: 0.34 |
| 01-architecture\network-topology.md | 39.1% | 66.7% | 38.2% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.38 |
| 04-security-and-compliance\rbac-model.md | 37.3% | 80.8% | 26.1% | ❌ | Section structure differs; Traceability references differ; Low content similarity: 0.26 |
| 06-quality\testing-and-validation.md | 35.3% | 69.4% | 28.9% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.29 |
| 05-operations-conops\operating-model.md | 34.9% | 69.4% | 28.2% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.28 |
| 03-data-and-ai\model-usage-and-guardrails.md | 34.2% | 75.0% | 23.4% | ❌ | YAML frontmatter differs; Traceability references differ; Low content similarity: 0.23 |
| 02-platform-components\shared-foundation-services.md | 30.3% | 66.7% | 20.5% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.21 |
| 06-quality\performance-and-scalability.md | 26.8% | 55.0% | 20.7% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.21 |
| 99-traceability\assumptions-risks-constraints.md | 23.5% | 48.1% | 18.2% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.18 |
| 02-platform-components\eva-chat.md | 23.3% | 48.1% | 17.8% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.18 |
| 02-platform-components\eva-domain-assistant.md | 21.4% | 48.1% | 14.0% | ❌ | YAML frontmatter differs; Section structure differs; Traceability references differ; Low content similarity: 0.14 |

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