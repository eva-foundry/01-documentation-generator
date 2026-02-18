# Documentation Generator Comparison Report

**Generated:** 2026-01-15T22:54:31.928576
**Original Output:** `..\..\generated-output-run-g`
**New Output:** `..\..\generated-output-run-h`

## Executive Summary

**Overall Consistency Score:** 100.00%

- **Files Analyzed:** 25
- **Identical:** 25 (100.0%)
- **Similar:** 0 (0.0%)
- **Different:** 0 (0.0%)
- **Missing:** 3

## Production Readiness Assessment

✅ **READY FOR PRODUCTION** - Generator demonstrates high consistency (≥85%)

## Per-File Comparison Matrix

| File | Overall Score | Structural | Content | Traceability | Issues |
|------|--------------|------------|---------|--------------|--------|
| 00-overview\executive-summary.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 00-overview\glossary-acronyms.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 00-overview\scope-in-out.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 01-architecture\logical-architecture.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 01-architecture\network-topology.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 01-architecture\physical-architecture.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 01-architecture\system-context.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 02-platform-components\eva-chat.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 02-platform-components\eva-domain-assistant.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 02-platform-components\shared-foundation-services.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 03-data-and-ai\data-ingestion-pipeline.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 03-data-and-ai\model-usage-and-guardrails.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 03-data-and-ai\prompt-and-config-governance.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 03-data-and-ai\rag-patterns.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 04-security-and-compliance\audit-and-logging.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 04-security-and-compliance\privacy-and-retention.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 04-security-and-compliance\rbac-model.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 04-security-and-compliance\security-architecture.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 05-operations-conops\backup-and-recovery.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 05-operations-conops\change-and-release.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 05-operations-conops\incident-and-contingency.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 05-operations-conops\onboarding-offboarding.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 05-operations-conops\operating-model.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 06-quality\accessibility.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 06-quality\testing-and-validation.md | 100.0% | 100.0% | 100.0% | ✅ | None |
| 06-quality\performance-and-scalability.md | N/A | N/A | N/A | N/A | File exists in only one output |
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

- ✅ Generator is production-ready for automated documentation generation
- ✅ Non-determinism is within acceptable bounds for AI-generated content
- ✅ Validation framework effectively ensures quality and traceability