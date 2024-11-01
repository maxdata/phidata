from phi.agent import Agent
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.exa import ExaTools
from phi.tools.yfinance import YFinanceTools
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app

web_agent = Agent(
    name="Web Agent",
    agent_id="web_agent",
    role="Search the web for information",
    model=AzureOpenAIChat(id="gpt-4o"),
    tools=[ExaTools()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent_sessions", db_file="tmp/agents.db"),
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    agent_id="finance_agent",
    role="Get financial data",
    model=AzureOpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent_sessions", db_file="tmp/agents.db"),
    markdown=True,
)

agent_team = Agent(
    name="Agent Team",
    agent_id="agent_team",
    team=[web_agent, finance_agent],
    storage=SqlAgentStorage(table_name="agent_team_sessions", db_file="tmp/agents.db"),
    markdown=True,
)

app = Playground(agents=[finance_agent, web_agent, agent_team]).get_app()

if __name__ == "__main__":
    serve_playground_app("cookbook.agents.agent_ui:app", reload=True)
