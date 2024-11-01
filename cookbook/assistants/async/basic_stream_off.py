import asyncio
from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-3.5-turbo"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)
# -*- Print a response to the cli
asyncio.run(assistant.async_print_response("Share a breakfast recipe.", markdown=True, stream=False))
