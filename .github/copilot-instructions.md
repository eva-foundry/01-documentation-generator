# GitHub Copilot Instructions Template

**Template Version**: 2.0.0  
**Generated**: January 29, 2026, 10:30 AM EST  
**Last Updated**: January 29, 2026  
**Project Type**: {PROJECT_TYPE}  
**Based on**: EVA Professional Component Architecture Standards (from EVA-JP-v1.2 production learnings)

---

## Release Notes

### Version 2.0.0 (January 29, 2026)
**Breaking Changes**:
- Transformed from project-specific to reusable template
- Added comprehensive placeholder system for all project-specific values
- Enhanced with anti-patterns prevention and quality gates

**New Features**:
- Template Usage Instructions section
- Anti-Patterns Prevention section
- Emergency Debugging Protocol
- File Organization Requirements
- Quality Gates checklist

**Improvements**:
- Complete PART 1 preservation (universal best practices)
- Structured placeholder guidance in PART 2
- Professional component implementations remain intact
- Enhanced documentation structure

### Version 1.0.0 (January 9, 2026)
**Initial Production Release**:
- Universal best practices (PART 1)
- EVA-JP-v1.2 project-specific patterns (PART 2)
- Professional Component Architecture (DebugArtifactCollector, SessionManager, StructuredErrorHandler, ProfessionalRunner)
- Azure account management patterns
- Workspace housekeeping principles
- Encoding safety standards

---

## Table of Contents

### PART 1: Universal Best Practices
- [Encoding & Script Safety](#critical-encoding--script-safety)
- [Azure Account Management](#critical-azure-account-management)
- [AI Context Management](#ai-context-management-strategy)
- [Azure Services Inventory](#azure-services--capabilities-inventory)
- [Professional Component Architecture](#professional-component-architecture)
  - [DebugArtifactCollector](#implementation-debugartifactcollector)
  - [SessionManager](#implementation-sessionmanager)
  - [StructuredErrorHandler](#implementation-structurederrorhandler)
  - [ProfessionalRunner](#implementation-zero-setup-project-runner)
- [Professional Transformation](#professional-transformation-methodology)
- [Dependency Management](#dependency-management-with-alternatives)
- [Workspace Housekeeping](#workspace-housekeeping-principles)
- [Code Style Standards](#code-style-standards)

#

## PART 2: 01-documentation-generator PROJECT SPECIFIC

> **AI-Powered Documentation Generator**  
> Status: Phase 2/6 Complete - Migration in Progress  
> Last Updated: January 29, 2026

### Documentation Guide

**Primary References**:
- **This file** (copilot-instructions.md): Quick reference workflows and patterns
- **[README.md](../README.md)**: Comprehensive project documentation
- **[PLAN.md](../PLAN.md)**: Migration roadmap and progress tracking (if exists)

### Architecture Overview

**System Type**: AI-Powered Documentation Generation System

**Core Components**:
- **EVAFoundationGenerator** ([src/generator.py](../src/generator.py), 776 lines): Main orchestration with Azure OpenAI integration, retry logic, state management
- **Validators** ([src/validators.py](../src/validators.py), 381 lines): 5-part validation (YAML, values, sections, consumability, traceability)
- **EvidenceCollector** ([src/evidence.py](../src/evidence.py), 348 lines): Requirement coverage analysis, traceability matrix, audit reports
- **Comparator** ([src/compare_outputs.py](../src/compare_outputs.py), 601 lines): Semantic document comparison and quality metrics

**Technology Stack**: Python 3.10+, Azure OpenAI (GPT-4), LangChain, pytest, Rich (console), PyYAML

**Critical Architecture Patterns**:
- **2-call handshake**: Optimized API pattern reducing calls from 4 to 2 (50% reduction)
- **Retry with validation feedback**: Max 3 attempts with structured error feedback to LLM
- **State persistence**: Resume capability after interruption via generation-state.json
- **Evidence collection**: Comprehensive audit trail for requirement traceability
- **5-part validation pipeline**: YAML → Values → Sections → Consumability → Traceability

### Project Structure

```
01-documentation-generator/
├── src/
│   ├── __init__.py              # Package exports (v0.1.0)
│   ├── generator.py             # EVAFoundationGenerator orchestrator (776 lines)
│   ├── validators.py            # Validation functions (381 lines)
│   ├── evidence.py              # EvidenceCollector class (348 lines)
│   ├── compare_outputs.py       # DocumentationComparator (601 lines)
│   └── config/                  # System prompts (future)
├── tests/
│   ├── __init__.py              # Test suite marker
│   └── test_generator.py       # Unit tests (394 lines, 19+ tests)
├── prompts/                     # YAML templates and exemplars
├── debug/                       # Debug artifacts (git-ignored)
├── sessions/                    # Session state checkpoints (git-ignored)
├── logs/                        # Generation logs (git-ignored)
├── requirements.txt             # 12 Python dependencies
├── pytest.ini                   # Test configuration
├── .env.example                 # Environment template
├── .env                         # Local config (git-ignored)
└── README.md                    # Main documentation
```

### Development Workflows

**Local Development Setup**:

```powershell
# 1. Navigate to project
cd i:\EVA-JP-v1.2\docs\eva-foundation\projects\01-documentation-generator

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure Azure OpenAI
Copy-Item .env.example .env
# Edit .env with your credentials

# 6. Verify installation
pytest tests/ -v
```

**Quick Commands**:
- **Test**: `pytest tests/ -v`
- **Test with coverage**: `pytest tests/ -v --cov=src --cov-report=html`
- **Test specific class**: `pytest tests/test_generator.py::TestYAMLValidation -v`
- **Watch mode**: `ptw tests/ -- -v` (requires pytest-watch)
- **Generate docs**: `python -m src.generator` (CLI coming in Phase 4)

### Critical Code Patterns

#### Pattern 1: YAML Frontmatter Validation

**Purpose**: Ensure all generated documents have valid metadata for traceability

**Implementation**:
```python
from src.validators import validate_yaml_frontmatter

content = """---
document_type: architecture
phase: 1
audience: [architects, developers]
traceability: [source-materials/requirements-v0.2/03_eva_chat_requirements.md]
---

# Document Content
"""

result = validate_yaml_frontmatter(content)
if not result["valid"]:
    print(f"[FAIL] {result['error']}")
```

**Required Fields**:
- `document_type`: architecture | technical_design | operational | governance | conops
- `phase`: Integer 0-7 or 99
- `audience`: List format (not inline)
- `traceability`: List of `source-materials/requirements-v0.2/FILE.md` paths

#### Pattern 2: Retry with Validation Feedback

**Purpose**: Retry AI generation until validation passes (max 3 attempts)

**Implementation**:
```python
from src.generator import EVAFoundationGenerator

# Generator automatically retries on validation failure
generator = EVAFoundationGenerator(
    workspace_root=Path.cwd(),
    dry_run=False,
    skip_validation=False
)

# Flow: Generate → Validate → Retry with feedback if failed
result = generator.generate_file(file_spec)
```

**Retry Strategy**:
- Max 3 attempts per file
- Validation errors sent as feedback to LLM
- Exponential backoff for timeouts (3s, 6s, 9s)
- Longer backoff for connection errors (5s, 10s, 15s)

#### Pattern 3: Evidence Collection

**Purpose**: Track requirement coverage and generate traceability reports

**Implementation**:
```python
from src.evidence import EvidenceCollector

evidence = EvidenceCollector(
    output_dir="../generated-output/markdown",
    eva_dir="../.."
)

# Analyze coverage
evidence.analyze_requirement_coverage()

# Generate report (JSON + Markdown)
report_path = evidence.generate_evidence_report()
print(f"[INFO] Evidence report: {report_path}")
```

**Output**: JSON + Markdown reports with requirement coverage matrix, traceability links, quality metrics

#### Pattern 4: 2-Call API Handshake

**Purpose**: Optimize API calls (50% reduction vs 4-call pattern)

**Implementation**:
```python
# Traditional: 4 calls (Role → Context → Exemplar → Generate)
# Optimized: 2 calls (Role+Context → Generate+Exemplar inline)

# Call 1: Setup with role and context
messages = [
    SystemMessage(content=role_prompt + context),
]

# Call 2: Generate with exemplar inline
messages.append(HumanMessage(
    content=f"Generate {filename}.\n\nFormat exemplar:\n{exemplar}"
))

response = await llm.ainvoke(messages)
```

**Benefits**: Faster generation, lower costs, improved reliability

### Testing

**Test Structure**:
- Tests located in: `tests/test_generator.py` (394 lines)
- Test classes: `TestYAMLValidation` (8 tests), `TestConsumabilityValidation` (4 tests), `TestTraceabilityValidation` (4 tests)
- Coverage target: >80%

**Running Tests**:
```powershell
# All tests with verbose output
pytest tests/ -v

# With coverage report (HTML output in htmlcov/)
pytest tests/ -v --cov=src --cov-report=html

# Specific test class
pytest tests/test_generator.py::TestYAMLValidation -v

# Skip slow integration tests
pytest tests/ -v -m "not integration"

# Watch mode (auto-rerun on file changes)
ptw tests/ -- -v
```

**Test Markers** (defined in [pytest.ini](../pytest.ini)):
- `@pytest.mark.unit` - Fast unit tests
- `@pytest.mark.integration` - Integration tests (require Azure OpenAI)
- `@pytest.mark.slow` - Slow-running tests

**Environment Configuration**:

**Required Variables** ([.env](../.env)):
```bash
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4

# Optional: Use Azure Identity instead of API key
USE_AZURE_IDENTITY=false

# Generation Configuration
MAX_TOKENS=4000
TEMPERATURE=0.7
TIMEOUT_SECONDS=180
```

**Azure Account Requirements**:
- Professional account: marco.presta@hrsdc-rhdcc.gc.ca
- Subscription: EsDAICoESub (d2d4e571-e0f2-4f6c-901a-f88f7669bcba)
- Resource: esdaicoe-ai-foundry-openai (Canada East)

### CI/CD Pipeline

**Status**: Not yet implemented (Phase 4 pending)

**Planned**:
- GitHub Actions workflow for automated testing
- Validation gate on PRs
- Evidence report generation on merge
- Automated deployment to shared location

### Troubleshooting

#### Issue 1: Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'langchain_openai'`  
**Cause**: Missing dependencies  
**Solution**: 
```powershell
pip install -r requirements.txt
```

#### Issue 2: Azure OpenAI 401 Unauthorized

**Symptom**: `AuthenticationError: Invalid API key`  
**Cause**: Missing or incorrect `.env` configuration  
**Solution**:
```powershell
# Verify .env exists
Test-Path .env

# Check environment variables loaded
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('AZURE_OPENAI_ENDPOINT'))"

# Verify account with Azure CLI
az account show --query user.name
```

#### Issue 3: Validation Failures

**Symptom**: Generated documents fail YAML validation  
**Cause**: AI model not following required schema  
**Solution**: Check system prompts in `src/config/` and update with examples. Retry with `--clean` flag.

#### Issue 4: Timeout Errors

**Symptom**: `TimeoutError` during API calls  
**Cause**: VPN instability or Azure OpenAI service delays  
**Solution**: Increase `TIMEOUT_SECONDS` in `.env` to 300 (5 minutes). Generator automatically retries with exponential backoff.

#### Issue 5: Tests Fail in Watch Mode

**Symptom**: `ptw: command not found`  
**Cause**: pytest-watch not installed  
**Solution**: `pip install pytest-watch`

### Performance Optimization

**Current Performance**:
- Single file generation: ~30-60 seconds (GPT-4)
- Validation overhead: ~1-2 seconds per file
- Full phase generation (10-15 files): ~10-15 minutes

**Optimization Strategies**:

1. **2-Call Handshake Pattern**: 50% reduction in API calls (from 4 to 2)
   - Traditional: Role → Context → Exemplar → Generate
   - Optimized: (Role+Context) → (Generate+Exemplar inline)
   - Implementation: [src/generator.py](../src/generator.py) lines 295-350

2. **Timeout Configuration**: 5-minute timeout for VPN stability
   - Default: 300 seconds (vs 180 seconds)
   - Configurable via `TIMEOUT_SECONDS` environment variable
   - Exponential backoff for retries: 3s, 6s, 9s

3. **Retry Strategy**: Intelligent retry with exponential backoff
   - Max 3 attempts per file
   - Timeout errors: 3s, 6s, 9s delay
   - Connection errors: 5s, 10s, 15s delay
   - Validation errors: Immediate retry with feedback

4. **State Persistence**: Avoid regenerating completed files
   - `generation-state.json` tracks completed files
   - Resume capability after interruption
   - Skip already-generated files on restart

5. **Token Tracking**: Approximate token counting (word count × 1.3)
   - Stored in state: `total_tokens`, `total_cost`
   - Displayed in summary table after generation

6. **Rich Console Streaming**: Real-time progress feedback
   - Spinners for long operations
   - Progress bars for batch processing
   - Formatted tables for summaries
   - Colored output for status

**Monitoring**:
- Generation logs: `logs/eva-foundation-generation.log`
- API call logs: `logs/api-calls-{timestamp}.log`
- Evidence reports: Track success rate and retry count
- Test coverage: `htmlcov/index.html` after `pytest --cov-report=html`

---

**For comprehensive project documentation, see [README.md](../README.md)**  
**For migration status, see [PLAN.md](../PLAN.md)** (if exists)
