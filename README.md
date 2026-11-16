# TelcoQA Copilot

Autonomous AI Assistant for Telco Test Generation & Gap Analysis built for the Agentic AI program.

## Features
- **Gherkin/BDD Test Generation**: Converts natural language telco feature descriptions into executable `.feature` files.
- **Playwright Automation Script**: Generates robust asynchronous Python Playwright scripts covering happy paths and fallback retry paths.
- **Coverage-Gap Report**: Automatically analyzes boundary values, timeout/retry paths, and malformed payloads in Markdown format.

## Tech Stack
- Python, Google GenAI SDK (`gemini-2.5-flash`), Playwright, Streamlit, Google Colab, GitHub.

## Project Structure
- `app.py`: Streamlit user interface.
- `copilot_engine.py`: Core AI agent logic.
- `features/`: Generated Gherkin BDD test scenarios.
- `tests/`: Runnable Playwright automation scripts.
- `reports/`: Coverage-gap analysis reports.
