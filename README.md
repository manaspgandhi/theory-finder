# Theory Finder

A research agent that, given a query about a TV show, autonomously searches the web (Reddit, Quora, etc.), gathers the latest theories, and summarizes them using an LLM (Gemini or OpenAI).

## Directory Structure

- `data_pipeline/` — Scrapers for Reddit, Quora, and other sources
- `agent/` — Orchestrates data collection
- `llm/` — Summarizes findings using an LLM
- `interface/` — CLI for user interaction
- `utils/` — Helper utilities

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Set up API keys for Reddit and LLMs
3. Run the CLI: `python interface/cli.py`

## TODO
- Implement Reddit and Quora scrapers
- Integrate Gemini or OpenAI for summarization
- Add more data sources
- Improve agent logic