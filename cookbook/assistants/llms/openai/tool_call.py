from phi.assistant import Assistant
from phi.llm.azure_chat import AzureOpenAIChat
from phi.tools.duckduckgo import DuckDuckGo


assistant = Assistant(llm=OpenAIChat(model="gpt-4-turbo"), tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)
