from phi.assistant import Assistant
from phi.llm.azure_chat import AzureOpenAIChat

assistant = Assistant(llm=OpenAIChat(model="gpt-4-turbo"), debug_mode=True, format_messages=False)
assistant.print_response(
    [
        {"role": "system", "content": "Reply with haikus."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)
