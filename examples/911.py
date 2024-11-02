from phi.agent import Agent
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.calculator import Calculator

agent = Agent(
    model=AzureOpenAIChat(id="gpt-4o"),
    # what is input parameter for calculator tool?
    # TODO: not sure how it works
    tools=[Calculator(add=True, subtract=True, multiply=True, divide=True)],
    instructions=["Use the calculator tool for comparisons."],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response(""""I have six candidates in triple backquotes    
    name: Ming; bill-rate: $49.50 Per Hour; available-date: 11/18/2024;
    name: Li; bill-rate: $50.00 Per Hour; available-date: 10/21/2024;
    name: Xia; bill-rate: $58.00 Per Hour; available-date: 11/04/2024;
    name: Wei; bill-rate: $55.00 Per Hour; available-date: 10/21/2024;
    name: Feng; bill-rate: $53.00 Per Hour; available-date: 11/18/2024;
    name: Zhao; bill-rate: $50.00 Per Hour; available-date: 11/11/2024;
    
    Show me all candidates with Bill Rate less than $55.
    """)
