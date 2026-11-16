```markdown
# Handover — Handbook Retrieval Fix

**Task.** Run python run_tests.py and verify that all 12 tests pass with 0 failures and 0 errors, and that handbook_late.md ranks first for the late-submission query.

**Resolved, and by whom.** The retrieval ranking issue was resolved by the agent in retrieve.py, which applies a 0.5 score multiplier when a document's source contains "superseded". During Phase 6, the agent also restored the expected document count from 7 to 6 in test_retrieve.py, after I confirmed that the change was accidental.

**Constraints.** The corpus/ directory must remain unchanged. The retrieval fix uses source metadata to reduce the ranking of superseded documents. Do not reintroduce the deliberate Phase 6 test failure or change the document-count expectation without justification. Remove private names and home-directory paths from shared evidence.

**Done.** The deliberate Phase 6 failure was undone by using python inject_failure.py --undo. The retrieval query was verified using `python retrieve.py "what is the penalty for late submission"`. The output confirmed that handbook_late.md ranks first. The final test command, python run_tests.py, reported:
  12 tests, 0 failures, 0 errors

**Next.** Review the final files and trace evidence, then submit the completed project and this handover document.

**Budget left.** No remaining budget has been tracked; the run was stopped after completing the required phases. Remaining Copilot usage has not been checked.
```

---

Two checks before you call it done:

- Could someone who was not in the room carry on from this alone? If not, which field is thin?
- Does it contain anything private — a real name, an email address, a full path with your username?
  Take it out now, not later.
