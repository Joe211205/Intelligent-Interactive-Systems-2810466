# Three bounded tasks. Pick one. (Step 1, 0–10 min)

A bounded task has three parts, and you write all three down before the agent starts:

1. **the task** — one sentence, in the imperative;
2. **the completion condition** — a command whose output decides it, not an opinion;
3. **the tool boundary** — what may be edited, what may be read, what is out of bounds.

If you cannot state the completion condition as a command, the task is not bounded yet. Narrow it
until you can. "Improve retrieval" is not a task. "Make `run_tests.py` green without editing
`corpus/`" is.

Task A is the one demonstrated. All three fit the 15 minutes you have for the agent run.

---

## Task A — fix a failure (the default)

**Task.** Make the current handbook outrank the superseded 2024 edition for the question
"what is the penalty for late submission".

**Why it matters.** Right now the retriever answers that question with a rule that was withdrawn in
2025. A student reading the assistant is told the wrong penalty, with provenance shown beside it,
which makes the wrong answer more convincing rather than less.

**Completion condition.**
```
python run_tests.py                                        -> 12 tests, 0 failures, 0 errors
python retrieve.py "what is the penalty for late submission"  -> handbook_late.md is the first hit
```

**Tool boundary.**
- may edit: `retrieve.py`, `tests/` (to add a test, not to weaken one)
- read-only: `corpus/`, `tools.py`
- not allowed: adding a dependency, network access, changing `run_tests.py`, running anything
  outside this folder

**Where the difficulty is.** The obvious fix — mark the file as superseded in its front matter — is
out of bounds, because `corpus/` is read-only. The available signal is already in the document's
`source` field. A good agent finds that; a hurried one edits the corpus anyway, and your AGENTS.md
is what stops it.

---

## Task B — add a feature

**Task.** Add a `--json` flag to `retrieve.py` that prints the hits as a JSON array, one object per
hit, keeping every provenance field.

**Completion condition.**
```
python retrieve.py --json "when is coursework 1 due" | python -c "import json,sys; d=json.load(sys.stdin); print(len(d), sorted(d[0]))"
python run_tests.py                                  -> 13 tests, 1 failures (task A's failure stays; it is not your job today)
```
The thirteenth test is yours: it asserts that every object carries `source`, `section`, `date` and
`score`.

**Tool boundary.** may edit `retrieve.py` and `tests/`; read-only `corpus/`, `tools.py`; no new
dependency (`json` is standard library).

**Where the difficulty is.** The existing print path must keep working exactly as it does now. An
agent that rewrites `__main__` wholesale usually breaks the human-readable output and does not
notice, because no test covers it. Say so in AGENTS.md.

---

## Task C — write tests

**Task.** Add three tests to `tests/test_tools.py` covering checks the suite does not reach yet:
a call with a missing `arguments` key, a call with `minutes` given as the string `"90"`, and the
log line written by a refused call.

**Completion condition.**
```
python run_tests.py   -> 15 tests, and you can say in one sentence what each new test protects
```

**Tool boundary.** may edit `tests/test_tools.py` only. `tools.py` is read-only: if a new test
fails, that is a finding to write down, not a licence to change the code.

**Where the difficulty is.** One of those three probably fails. Deciding whether the test or the
tool is wrong is the skill; an agent that quietly edits `tools.py` to make its own test pass has
told you something useful about how you wrote the boundary.
