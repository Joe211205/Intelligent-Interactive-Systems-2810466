```markdown
# AGENTS.md

## Project overview
This repository contains a small Python retrieval system and test suite. The project uses lexical retrieval over local documents and does not use a vector store or external APIs. The goal is to retrieve relevant passages while preserving provenance information.

## Build and test
python retrieve.py --selftest
python run_tests.py

## Conventions
- every retrieved passage keeps its source, section and date
- retrieval results should preserve provenance information
- tests should pass without adding external dependencies

## Never
- do not edit anything under corpus/
- do not add dependencies; use only the Python standard library
- do not weaken or remove tests to make a run pass
- do not modify handbook documents

## When you are unsure
- stop and ask, describing the two possible interpretations before proceeding
```
