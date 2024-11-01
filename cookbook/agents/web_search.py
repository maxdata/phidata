"""Run `pip install openai duckduckgo-search` to install dependencies."""

from phi.agent import Agent
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.exa import ExaTools

web_agent = Agent(
    name="Web Agent",
    model=AzureOpenAIChat(id="gpt-4o"),
    tools=[ExaTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Whats happening in France?", stream=True)
