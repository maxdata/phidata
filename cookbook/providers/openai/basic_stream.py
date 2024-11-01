from typing import Iterator  # noqa
from phi.agent import Agent, RunResponse  # noqa
from phi.llm.azure_chat_model import AzureOpenAIChat

agent = Agent(model=OpenAIChat(id="gpt-4o"), markdown=True)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
