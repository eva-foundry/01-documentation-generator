# Document Templates

This directory contains YAML templates defining the structure and requirements for each documentation file.

## Purpose

Templates specify:
- Document structure (sections, subsections)
- Required content elements
- Cross-references to other documents
- Validation rules
- Evidence requirements

## Template Format

Each template is a YAML file with the following structure:

```yaml
name: "Document Name"
phase: 0
output_file: "section/filename.md"
dependencies:
  - "other-file.md"
sections:
  - title: "Section Title"
    required: true
    description: "What this section should contain"
    validation_rules:
      - "Rule description"
evidence_sources:
  - "Path to source files"
```

## Files

Templates are organized by phase:
- **Phase 0**: Overview documents (README, glossary, architecture)
- **Phase 1**: Core infrastructure and deployment
- **Phase 2**: Application architecture (backend, frontend, functions)
- **Phase 3**: Features and capabilities
- **Phase 4**: Operations and monitoring
- **Phase 5**: Security and compliance
- **Phase 6**: Testing and quality assurance
- **Phase 7**: Development and contribution guides

## Usage

Templates are processed by the generator to:
1. Create generation prompts with specific requirements
2. Validate generated content against expected structure
3. Ensure cross-reference consistency
4. Track evidence usage

## Migration Status

✅ **Complete**: Templates extracted from `automation/generate-docs.py` CONTENT_SPECS and moved to `src/generator.py` (Phase 3 complete).

🔮 **Future Enhancement**: Separate YAML template files (pending Phase 4 refactoring).
