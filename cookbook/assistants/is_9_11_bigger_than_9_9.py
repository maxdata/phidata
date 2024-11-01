from phi.assistant import Assistant
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.calculator import Calculator

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-4o"),
    tools=[Calculator(add=True, subtract=True, multiply=True, divide=True)],
    instructions=["Use the calculator tool for comparisons."],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("Is 9.11 bigger than 9.9?")
assistant.print_response("9.11 and 9.9 -- which is bigger?")
