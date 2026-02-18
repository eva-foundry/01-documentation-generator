# Documentation Generator Comparison Report

**Generated:** 2026-01-15T18:13:53.451536
**Original Output:** `..\..\generated-output-run-a`
**New Output:** `..\..\generated-output`

## Executive Summary

**Overall Consistency Score:** 46.20%

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
| 04-security-and-compliance\audit-and-logging.md | 70.8% | 65.0% | 62.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.63 |
| 03-data-and-ai\model-usage-and-guardrails.md | 69.2% | 63.1% | 60.5% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.60 |
| 01-architecture\physical-architecture.md | 60.3% | 79.2% | 33.1% | ✅ | Section structure differs; Low content similarity: 0.33 |
| 03-data-and-ai\rag-patterns.md | 59.5% | 58.3% | 44.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.44 |
| 06-quality\performance-and-scalability.md | 58.8% | 25.0% | 62.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.63 |
| 00-overview\glossary-acronyms.md | 57.8% | 75.0% | 30.7% | ✅ | YAML frontmatter differs; Low content similarity: 0.31 |
| 05-operations-conops\onboarding-offboarding.md | 54.4% | 41.0% | 44.2% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.44 |
| 01-architecture\system-context.md | 53.3% | 68.5% | 25.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.26 |
| 05-operations-conops\change-and-release.md | 53.0% | 78.6% | 18.8% | ✅ | Section structure differs; Low content similarity: 0.19 |
| 03-data-and-ai\data-ingestion-pipeline.md | 50.8% | 67.1% | 21.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.21 |
| 00-overview\executive-summary.md | 50.7% | 45.0% | 34.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.34 |
| 02-platform-components\eva-chat.md | 49.7% | 65.0% | 20.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 06-quality\testing-and-validation.md | 43.8% | 39.3% | 24.1% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.24 |
| 02-platform-components\eva-domain-assistant.md | 42.7% | 46.1% | 17.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.18 |
| 03-data-and-ai\prompt-and-config-governance.md | 41.6% | 42.4% | 17.7% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.18 |
| 04-security-and-compliance\security-architecture.md | 41.4% | 37.5% | 20.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.20 |
| 01-architecture\logical-architecture.md | 40.5% | 25.0% | 25.9% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.26 |
| 05-operations-conops\backup-and-recovery.md | 39.6% | 41.0% | 14.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.15 |
| 04-security-and-compliance\privacy-and-retention.md | 39.6% | 25.0% | 24.1% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.24 |
| 02-platform-components\shared-foundation-services.md | 38.7% | 25.0% | 22.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.22 |
| 99-traceability\requirements-mapping.md | 38.3% | 37.0% | 14.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.14 |
| 06-quality\accessibility.md | 37.0% | 37.5% | 11.4% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.11 |
| 00-overview\scope-in-out.md | 35.8% | 25.0% | 16.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.17 |
| 05-operations-conops\operating-model.md | 35.6% | 34.4% | 10.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.11 |
| 99-traceability\assumptions-risks-constraints.md | 33.8% | 25.0% | 12.6% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.13 |
| 05-operations-conops\incident-and-contingency.md | 32.9% | 25.0% | 10.8% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.11 |
| 01-architecture\network-topology.md | 32.2% | 25.0% | 9.3% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.09 |
| 04-security-and-compliance\rbac-model.md | 32.0% | 25.0% | 9.0% | ✅ | YAML frontmatter differs; Section structure differs; Low content similarity: 0.09 |

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