from phi.agent import Agent
from phi.llm.azure_chat_model import AzureOpenAIChat

task = (
    "I have six candidates in triple backquotes\n"
    "```\n"
    "name: Ming; bill-rate: $49.50 Per Hour; available-date: 11/18/2024;\n"
    "name: Li; bill-rate: $50.00 Per Hour; available-date: 10/21/2024;\n"
    "name: Xia; bill-rate: $58.00 Per Hour; available-date: 11/04/2024;\n"
    "name: Wei; bill-rate: $55.00 Per Hour; available-date: 10/21/2024;\n"
    "name: Feng; bill-rate: $53.00 Per Hour; available-date: 11/18/2024;\n"
    "name: Zhao; bill-rate: $50.00 Per Hour; available-date: 11/11/2024;\n"
    "```\n"
    "Show me all candidates with Bill Rate less than $55."
)

# Ethan Doe; bill-rate: $53.00 Per Hour missed

reasoning_agent = Agent(model=AzureOpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True, debug_mode=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
