from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat

topic = "ice cream"
assistant = Assistant(llm=AzureOpenAIChat(model="gpt-3.5-turbo"))
assistant.print_response(f"Tell me a joke about {topic}")
