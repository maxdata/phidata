from phi.agent import Agent
from phi.llm.azure_chat_model import AzureOpenAIChat

agent = Agent(
    model=AzureOpenAIChat(id="gpt-4o"),
    markdown=True,
)

agent.print_response(
    "What are in these images? Is there any difference between them?",
    images=[
        "https://cdn-ilalkbd.nitrocdn.com/FarPNdpFBRtkiJviAsBGjVXNCdUeAZKT/assets/images/optimized/rev-bfc21bb/leanstartup.co/wp-content/uploads/2017/10/board-361516_1920.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
    ],
)
