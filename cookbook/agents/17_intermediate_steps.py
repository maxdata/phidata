from typing import Iterator
from rich.pretty import pprint
from phi.agent import Agent, RunResponse
from phi.llm.azure_chat_model import AzureOpenAIChat
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=AzureOpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
    show_tool_calls=True,
)

run_stream: Iterator[RunResponse] = agent.run(
    "What is the stock price of NVDA", stream=True, stream_intermediate_steps=True
)
for chunk in run_stream:
    pprint(chunk.model_dump(exclude={"messages"}))
    print("---" * 20)
