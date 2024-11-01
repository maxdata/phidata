from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-4o"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)
# -*- Print a response to the cli
assistant.print_response("Share a breakfast recipe.", markdown=True)
