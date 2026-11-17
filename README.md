# Explainable AI assistant

README word count: 344

An AI assistant made to increase transparency and trust by giving evidence-backed responses, clarification mechanisms and uncertainty handling.

## Project Status
This project explores how transparency and explainability can help users find mistakes in AI generated responses.

Implemented features:
- Conversational question and answer interface
- Evidence and source display alongside answers
- Retrieval of information from a document corpus
- Clarification for ambiguous requests
- Refusal of unsupported or unanswerable questions
- Uncertainty and confidence handling 
- Tool validation and confirmation before execution

Simulated features:
- Extended explanation generation for some interaction scenarios

Planned features:
- Additional personalisation options
- More advanced explanation generation
- Improved confidence calibration

## Technology stack
- Python: Main application logic and backend processing.
- HTML: structure of the web interface.
- Retrieval module (`retrieve.py`): Searches the document corpus for relevant supporting information.
- JavaScript: Frontend interaction with the assistant.
- Tool validation module (`tools.py`): handles proposed actions, validation and user confirmation
- vision-language module (`vlm.py`): Supports image-based queries.
- GitHub: version control and project hosting

## Running the Project

1. Open the terminal inside the project folder.
2. run:
  ```bash
  python app.py
  ```
3. Open:
  ```text
  http://localhost:8000/
  ```
4. Interact with the assistant through the web interface

## development record
### Week 1
- defined the project problem and research question.
- Performed literature review on explainability, trust and transparency in AI systems.

### week 2
- Developed interaction storyboards
- Created user journeys, failure scenarios and recovery paths.

### Week 3
- Produced system specification and architecture.
- defined user inputs, processing stages, fallback behaviour and outputs

### Week 4
- implemented retrieval-based responses
- Added evidence display and source information.
- Implemented confidence handling and unsupported answer refusal
- added tool validation and confirmation workflows.

### Week 5
- Conducted verification activities and testing
- documented agent behaviour, development evidence and planning.

## AI assistance
ChatGPT was used to help with:
- brainstorming design ideas
- Reviewing implementation approaches
- Clarifying technical concepts
- supporting report preparation and documentation

GitHub Copilot was used to review the supplied code and support development, as required during the labs.

All generated content was reviewed, checked and edited before inclusion in the final project.

## Additional Files
the repository contains:
- source code
- system diagrams
- development documentation
- assignment materials
- report related assets and screenshots.
