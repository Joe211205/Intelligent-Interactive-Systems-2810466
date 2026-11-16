# COMPARISON

| | agentic run | direct prompting |
|---|---|---|
| steps you could see | 13 | 5 |
| times you intervened | Multiple | 1 |
| minutes, start to green | 44s | 114s |
| outcome | 12 passed, 0 failures, 0 errors| 12 passed, 0 failures, 0 errors |

The agentic run did more than just suggest a fix. It inspected the project instructions and relevant files, checked the retrieval scores. It then edited retrieve.py, ran the tests and investigated failure during Phase 6.
Some of these actions happened without me having to carry them out manually, although I still had to intervene when it used the wrong working directory as well as when it needed confirmation before changing the test expectation.
This meant waiting for the agent to complete its steps and checking that it had followed the project instructions.
The trace additionally showed details that I normally wouldn't see in a direct chat, such as which files it inspected, commands it ran, the original and updated retrieval scores and how it investigated and recovered from an error.
Direct prompting was more manual because I had to apply the recommended change and run tests myself, but it was still successful and took 114 seconds compared with 44 seconds for the agentic fix.
Overall, the agentic approach gave me a clearer record of the process, whereas direct prompting gave me more direct control over each change.
