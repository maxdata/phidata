from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("Search for news from France and write a short poem about it.")
