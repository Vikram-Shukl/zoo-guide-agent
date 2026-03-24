import os
import logging
import wikipedia
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext

logging.basicConfig(level=logging.INFO)
load_dotenv()

model_name = os.getenv("MODEL", "gemini-2.5-flash")

def add_prompt_to_state(
    tool_context: ToolContext, prompt: str
) -> dict[str, str]:
    """Saves the user's initial prompt to the state."""
    tool_context.state["PROMPT"] = prompt
    logging.info(f"[State updated] Added to PROMPT: {prompt}")
    return {"status": "success"}

def search_wikipedia(query: str) -> dict[str, str]:
    """Search Wikipedia for information about animals and return a summary."""
    try:
        result = wikipedia.summary(query, sentences=5)
        return {"result": result}
    except Exception as e:
        return {"result": f"Could not find information: {str(e)}"}

comprehensive_researcher = Agent(
    name="comprehensive_researcher",
    model=model_name,
    description="Researcher that searches Wikipedia for animal information.",
    instruction="""
You are a helpful research assistant. Answer the user's PROMPT by searching Wikipedia.
Use the search_wikipedia tool to find relevant information.

PROMPT:
{ PROMPT }
""",
    tools=[search_wikipedia],
    output_key="research_data"
)

response_formatter = Agent(
    name="response_formatter",
    model=model_name,
    description="Synthesizes all information into a friendly, readable response.",
    instruction="""
You are the friendly voice of the Zoo Tour Guide. Take the RESEARCH_DATA
and present it to the user in a complete, helpful, and engaging way.

RESEARCH_DATA:
{ research_data }
"""
)

tour_guide_workflow = SequentialAgent(
    name="tour_guide_workflow",
    description="The main workflow for handling a user's request about an animal.",
    sub_agents=[comprehensive_researcher, response_formatter]
)

root_agent = Agent(
    name="greeter",
    model=model_name,
    description="The main entry point for the Zoo Tour Guide.",
    instruction="""
Welcome the user to the Zoo Tour Guide!
When the user asks about an animal, use 'add_prompt_to_state' tool to save their query,
then transfer control to 'tour_guide_workflow'.
""",
    tools=[add_prompt_to_state],
    sub_agents=[tour_guide_workflow]
)
