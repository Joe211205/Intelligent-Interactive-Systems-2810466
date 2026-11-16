# AGENTS.md — template

Copy this file to `AGENTS.md` in the root of this repository and fill it in. Delete the bracketed
prompts as you go; they are for you, not for the agent.

Rules of thumb from Lecture 15:

- **Half a page.** Every line is in the context window on every call. A file nobody finishes reading
  is also a file you pay for on every turn.
- **Commands that actually run.** Type each one before you write it down. An AGENTS.md that says
  `pytest -q` in a repository with no pytest is worse than no file at all, because it is believed.
- **Only what is true of every task here.** Anything true of one kind of task is a skill. Anything
  true of today only — a name, a date, a chosen task — is state, and belongs nowhere near this file.

---

```markdown
# AGENTS.md

## Project overview
[Two or three lines. What this repository is, what language and version, and one thing that would
surprise someone: "retrieval is lexical; there is no vector store."]

## Build and test
[The exact commands. Ours are:]
python retrieve.py --selftest
python run_tests.py

## Conventions
[Two or three that you actually care about. Ours, for example:]
- every retrieved passage keeps its source, section and date
- no tool call runs without valid() and a confirmation

## Never
[The boundary for today's task, written so it holds tomorrow as well.]
- do not edit anything under corpus/
- do not add a dependency; the standard library is the whole toolbox
- do not weaken a test to make a run pass

## When you are unsure
[One line. This is the line that decides whether the agent guesses or asks.]
- stop and ask, with the two readings written out
```
