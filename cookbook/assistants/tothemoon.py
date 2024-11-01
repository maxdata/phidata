from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-4o"),
    description="You are a rocket scientist",
)
assistant.print_response("write a plan to go to the moon stp by step", markdown=True)
