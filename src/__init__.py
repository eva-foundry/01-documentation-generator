"""
EVA Foundation Documentation Generator

A modular documentation generation system using Azure OpenAI.
"""

from .generator import (
    EVAFoundationGenerator,
    FileSpec,
    ValidationResult
)

from .validators import (
    validate_phase_content,
    validate_file_completeness,
    validate_cross_references,
    validate_markdown_syntax,
    validate_all_documents
)

from .evidence import (
    EvidenceCollector,
    save_evidence,
    load_evidence
)

__version__ = "0.1.0"
__all__ = [
    "EVAFoundationGenerator",
    "FileSpec",
    "ValidationResult",
    "validate_phase_content",
    "validate_file_completeness",
    "validate_cross_references",
    "validate_markdown_syntax",
    "validate_all_documents",
    "EvidenceCollector",
    "save_evidence",
    "load_evidence"
]
