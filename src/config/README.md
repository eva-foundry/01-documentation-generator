# System Prompts Configuration

This directory contains system prompts and configuration templates for the documentation generator.

## Purpose

System prompts define the behavior and constraints for the AI model when generating documentation. They ensure:
- Consistent output quality
- Proper formatting and structure
- Domain-specific knowledge application
- Validation rules adherence

## Structure

Configuration files should be organized by:
- **Phase**: Each documentation phase may have specific prompts
- **Type**: Different document types (overview, technical, governance)
- **Purpose**: Generation, validation, refinement

## Files

- `base_system_prompt.yaml` - Core system instructions
- `phase_prompts.yaml` - Phase-specific generation prompts
- `validation_prompts.yaml` - Content validation instructions

## Usage

System prompts are loaded by the generator and combined with:
1. Document template requirements
2. Context from previous phases
3. Evidence from source files
4. Cross-reference constraints

## Migration Status

✅ **Complete**: System prompts migrated from `automation/generate-docs.py` to `src/generator.py` (Phase 3 complete).
