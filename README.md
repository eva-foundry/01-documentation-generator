# EVA Foundation - Documentation Generator

**Status:** Migration from `automation/` in progress (Phase 2 complete)

A modular, AI-powered documentation generation system for the EVA Foundation project. This tool uses Azure OpenAI to generate comprehensive, validated, and traceable documentation from source code and requirements.

## Overview

This documentation generator is designed to:

- **Generate AI-consumable documentation** from source code, requirements, and existing documentation
- **Validate content quality** using automated checks for YAML frontmatter, consumability patterns, and traceability
- **Track evidence** of requirement coverage and implementation linkage
- **Support incremental generation** with phase-based approach and state management
- **Provide audit trails** through comprehensive evidence reports

## Project Structure

```
01-documentation-generator/
├── src/
│   ├── __init__.py              # Package initialization with exports
│   ├── validators.py            # Content validation functions
│   ├── evidence.py              # Evidence collection and reporting
│   └── config/
│       └── README.md            # System prompts documentation
├── tests/
│   ├── __init__.py              # Test suite marker
│   └── test_generator.py        # Unit tests for validators
├── prompts/
│   └── README.md                # YAML templates documentation
├── docs/
│   └── (future migration docs)
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment configuration template
├── .gitignore                   # Git ignore rules
├── pytest.ini                   # Test configuration
└── README.md                    # This file
```

## Features

### Completed (Migrated from automation/)

- **Validators Module** (`src/validators.py`)
  - YAML frontmatter validation
  - AI-consumability checks (tables, code blocks, explicit references)
  - Requirement traceability validation
  - Cross-reference validation
  - Markdown syntax validation

- **Evidence Module** (`src/evidence.py`)
  - File generation tracking
  - Requirement coverage analysis
  - Traceability matrix generation
  - Quality metrics calculation
  - Evidence report generation (JSON + Markdown)

- **Test Suite** (`tests/test_generator.py`)
  - Unit tests for all validators
  - Parametrized tests for requirement ID formats
  - Integration test placeholders
  - Test fixtures for valid/invalid content

### Pending Migration (See PLAN.md)

- **Generator Module** (Phase 3)
  - Main generation orchestration
  - Azure OpenAI integration
  - Retry logic with validation
  - State management

- **Configuration System** (Phase 3)
  - System prompts (src/config/)
  - Document templates (prompts/)
  - Content specifications

- **CLI Interface** (Phase 4)
  - Command-line interface
  - Phase selection
  - Progress reporting

## Setup Instructions

### 1. Prerequisites

- Python 3.10+
- Azure OpenAI account (for generation phase)
- VS Code (recommended)

### 2. Installation

```powershell
# Navigate to project directory
cd c:\Users\marco.presta\dev\AICOE\EVA-Jurisprudence-SecMode-Info-Assistant-v1.2\docs\eva-foundation\projects\01-documentation-generator

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```powershell
# Copy environment template
Copy-Item .env.example .env

# Edit .env with your Azure OpenAI credentials
notepad .env
```

Required environment variables:
- `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI endpoint URL
- `AZURE_OPENAI_API_KEY` - Your API key (or use Azure Identity)
- `AZURE_OPENAI_DEPLOYMENT_NAME` - Your GPT-4 deployment name

### 4. Run Tests

```powershell
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html

# Run specific test class
pytest tests/test_generator.py::TestYAMLValidation -v
```

## Usage (After Full Migration)

### Basic Generation

```python
from src.validators import validate_all_documents
from src.evidence import EvidenceCollector

# Validate existing documentation
results = validate_all_documents("../output")
print(f"Passed: {results['passed']}/{results['total']}")

# Collect evidence
evidence = EvidenceCollector(
    output_dir="../output",
    eva_dir="../.."
)
evidence.analyze_requirement_coverage()
report_path = evidence.generate_evidence_report()
print(f"Evidence report: {report_path}")
```

### CLI (Coming in Phase 4)

```powershell
# Generate all phases
python -m src.cli generate --all

# Generate specific phase
python -m src.cli generate --phase 1

# Validate existing output
python -m src.cli validate --output-dir ../output

# Generate evidence report
python -m src.cli evidence --output-dir ../output
```

## Migration Status

Track the migration progress in [PLAN.md](PLAN.md). Current status:

- Phase 1: Analysis and planning (Complete)
- Phase 2: Scaffolding and module migration (Complete)
- Phase 3: Core generator migration (In Progress)
- Phase 4: CLI and integration (Pending)
- Phase 5: Testing and validation (Pending)
- Phase 6: Documentation and cleanup (Pending)

## Development

### Running Tests During Development

```powershell
# Watch mode (requires pytest-watch)
ptw tests/ -- -v

# Test specific module
pytest tests/test_generator.py::TestConsumabilityValidation -v

# Skip slow integration tests
pytest tests/ -v -m "not integration"
```

### Adding New Validators

1. Add validation function to `src/validators.py`
2. Add corresponding tests to `tests/test_generator.py`
3. Update exports in `src/__init__.py`
4. Document in this README

### Code Quality

This project follows:
- **Black** for code formatting (line length 180)
- **isort** for import sorting
- **pytest** for testing (target >80% coverage)
- **Type hints** for all public functions
- **Docstrings** for all modules, classes, and functions

## Related Documentation

- **Migration Plan**: [PLAN.md](PLAN.md) - Detailed migration steps
- **System Prompts**: [src/config/README.md](src/config/README.md) - Prompt configuration guide
- **Templates**: [prompts/README.md](prompts/README.md) - Document template specification
- **Original Automation**: `../../automation/` - Source of migrated code

## Contributing

This is an internal tool for the EVA Foundation project. For questions or issues:

1. Check [PLAN.md](PLAN.md) for migration status
2. Review existing tests in `tests/test_generator.py`
3. Follow code quality standards above

## License

Internal use only - EVA Foundation project.

---

**Last Updated:** January 15, 2026  
**Migration Phase:** 2/6 (Scaffolding Complete)
