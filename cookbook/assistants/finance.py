from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    add_chat_history_to_messages=True,
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)
assistant.print_response("What is the stock price of NVDA")
assistant.print_response("Write a comparison between NVDA and AMD, use all tools available.")
