# Zoo Guide AI Agent

An AI-powered Zoo Tour Guide Agent built using Google Agent Development Kit (ADK) and Gemini, deployed on Cloud Run.

## Overview

This agent helps zoo visitors learn about animals by:
- Answering questions about animals using Wikipedia
- Providing a friendly, conversational experience
- Running as a serverless application on Google Cloud Run

## Tech Stack

- **Google ADK** - Agent Development Kit
- **Gemini 2.5 Flash** - AI Model
- **Cloud Run** - Serverless Deployment
- **Wikipedia API** - Knowledge Source
- **LangChain** - Tool Integration

## Project Structure
```
zoo_guide_agent/
├── agent.py          # Main agent code
├── __init__.py       # Package init
├── requirements.txt  # Dependencies
└── .env              # Environment variables
```

## Live Demo

🚀 **Cloud Run URL:** https://zoo-tour-guide-510759398565.us-central1.run.app

## How to Run

1. Clone the repo:
```
git clone https://github.com/Vikram-Shukl/zoo-guide-agent.git
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Deploy to Cloud Run:
```
adk deploy cloud_run --project=YOUR_PROJECT_ID --region=us-central1 --service_name=zoo-tour-guide --with_ui .
```

## Agent Architecture

- **Greeter Agent** - Welcomes users and saves their query
- **Researcher Agent** - Searches Wikipedia for information  
- **Formatter Agent** - Presents information in a friendly way

## Submitted By

- **Name:** Vikram Shukla
- **Email:** vikramshukl990@gmail.com
- **Hackathon:** Gen AI Academy APAC Edition - Track 1
