# 01_SPEC.md: use case and system path

Use this file for the use case from your Week 2 storyboard. Keep the notes short enough to use while you work.

## User goal
<What is the person trying to achieve?>
The user is trying to understand not only the AI assistant's answer, but at the same time know the reasoning behind it so mistakes and incorrect assumptions can be identified.
## System inputs
<What does the person provide, and what data or context does the system receive?>
The user provides question, follow-up questions and  requests for clarification.
The system receives user query, conversation history and context from previous interactions.
## Processing and technology
<What does the system extract, look up, classify, generate or decide? Which model, tool, data source or software component would carry out each important step?>
Extract: User question, task request, feedback and conversation context; Natural Language Processing module.
Classify: determine user intent and whether more explaining or clarification needed; Intent classification model.
Generate: produce an answer to the user's question with a short explanation of reasoning; Large Language Model (LLM).
Decide: estimate confidence, detect guesses and missing information, identify uncertainty; Confidence/uncertainty assessment module.
Present: display the answer, uncertainty indicator, reasoning and potential next steps through a chat interface; User interface (AI assistant).
## Intended result and next action
<What does the system return, and what can the person do next?>
System returns:
    - answer to user question
    - short explanation of reasons
    - uncertainty indicator if answer could be untrustworthy
    - suggestions for verification or next steps

User can next:
    - use answer to complete their task
    - check reasons for potential errors or assumptions
    - ask for more justification
    - provide extra information and continue conversation
## Fallback strategy
<What happens if information is missing, ambiguous, outside the system's scope or unavailable?>
missing info: ask the user for clarification or more detail.
ambiguous question: give potential interpretations and ask the user to pick the intended meaning.
uncertain system: display an uncertainty indicator and justify assumptions made.
outside system's knowledge or scope: say the limitation and suggest other sources or verification methods.
user misunderstanding: give a more detailed explanation and expect follow-up questions.

## System path or interaction diagram
Add a flowchart, use-case diagram or system architecture sketch showing the person, input, processing, data or model or tool, response and next action. Label anything that is implemented, simulated or still planned.

File in zip.

## Test A: standard input
Input:"How do I complete this task?"

What the system receives:
    - User question
    - Conversation context
    - Task request

What it does:
    - Identifies user intent
    - Generates an answer
    - Generates a short justification for reasoning

Response and next action:
    - Returns the answer, reasoning, confidence/uncertainty level and suggested next steps
    - User understands the justification and uses the answer to complete the task or ask a follow-up question

## Test B: problem input
Input: User asks a question but does not understand the answer provided.

What the system receives:
    - User question
    - Conversation context

What it does:
    - Generates an answer
    - Wrongly assumes the user understands response
    - Provides little or no explanation

Response and next action:
    - User receives an answer but is unsure how it was produced
    - User notices the missing reasoning and asks for clarification.
    - User asks: "Can you explain how you got that answer?"

## Review and revision
Use the tests to identify an interaction or system problem. Note the evidence, then describe one interaction change and one technology or system change. Explain why the changes help and run Test B again.

Problem identified: The system assumes the user understands the response as well as not always providing enough explanation.

Evidence: In Test B, the user received an answer but could not understand how it was made and had to request clarification.

Interaction change: Automatically display a short explanation and uncertainty indicator with every response.

Why it helps: Users can understand the justification immediately and are therefore more likely to find errors or wrong assumptions.

Technology/system change: Include an explanation-generation module that creates reasoning and confidence information alongside all answers.

Why it helps: Improve transparency, user's ability to verify answers and trust.

# TEST B AFTER REVISION
Input: User asks a question but is unsure how the answer was reached.

What the system receives:
    - User question
    - Conversation context

What it does:
    - Creates a response
    - Generates a small explanation of reasoning
    - Shows confidence/uncertainty information

Response and next steps:
    - User receives the response, justification, confidence level and recommended next steps.
    - User understands how the answer was created and can either complete the task or query the system with a follow-up question.