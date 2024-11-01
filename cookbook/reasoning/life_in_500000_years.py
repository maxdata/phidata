from phi.agent import Agent
from phi.llm.azure_chat_model import AzureOpenAIChat

task = "Write a short story about life in 500000 years"

reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
