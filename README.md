# Agentic Research Orchestrator for Developers

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-State_Management-orange)
![Firecrawl](https://img.shields.io/badge/Firecrawl-Web_Scraping-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT_4o-green)

This project implements an **autonomous agentic workflow** capable of performing deep technical research. Unlike simple linear scripts or basic RAG systems, this agent uses a graph-based architecture to plan, search, scrape, and synthesize information iteratively.

It is designed to take a high-level query (e.g., *"Compare Supabase vs Firebase for a scalable chat app"*) and output a comprehensive, data-backed report by autonomously navigating web documentation.

## Features
* **Graph-Based Orchestration:** Built using **LangGraph** to manage state and define cyclical workflows (loops) rather than linear chains.
* **Autonomous Web Navigation:** Utilizes **Firecrawl** to scrape specific sub-pages and extract clean markdown from technical documentation.
* **Structured Output:** Synthesizes gathered data into a structured report saved automatically to the local file system.
* **Self-Correction:** The agent analyzes its own search results to determine if more depth is needed before finalizing the answer.

## Tech Stack
* **Orchestration Framework:** LangGraph (LangChain)
* **LLM:** GPT-4o / GPT-4o-mini
* **Web Scraper:** Firecrawl API
* **Environment Management:** `uv` (modern Python package manager)
* **Language:** Python

##  How It Works
The system follows a Directed Acyclic Graph (DAG) architecture:
1.  **Input:** User provides a research topic.
2.  **Search Node:** The agent generates search queries to find relevant documentation.
3.  **Process Node:** Scrapes the content using Firecrawl.
4.  **Decision Edge:** The LLM evaluates if the data is sufficient.
    * *If yes:* Move to generation.
    * *If no:* Loop back to search with refined queries.
5.  **Output:** Generates a final Markdown report.


## Acknowledgements 
This project was built as an implementation of advanced agentic patterns, inspired by the "Advanced Research Agent" architecture demonstrated by Tech With Tim. It serves as a study in modern stateful AI systems.
##  Installation & Usage


   ```bash
   git clone [https://github.com/busetolunay/Agentic-Developer-Scout.git](https://github.com/busetolunay/Agentic-Developer-Scout.git)
   cd Agentic-Research-Orchestrator

   #create a .env file in root directory and add your keys 
   OPENAI_API_KEY="sk-..."
   FIRECRAWL_API_KEY="fc-..."
   #install dependencies
   uv sync
   
   # for advanced agent 
   uv run advance-agent/main.py
   #
   uv run advance-agent/main.py 
   ```
