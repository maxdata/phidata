"""Run `pip install duckdb` to install dependencies."""

import json

from phi.llm.azure_chat_model import AzureOpenAIChat    
from phi.agent.duckdb import DuckDbAgent

data_analyst = DuckDbAgent(
    model=AzureOpenAIChat(id="gpt-4o"),
    markdown=True,
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        },
        indent=2,
    ),
)
data_analyst.print_response(
    """I have six candidates in triple backquotes    
    name: Ming; bill-rate: $49.50 Per Hour; available-date: 11/18/2024;
    name: Li; bill-rate: $50.00 Per Hour; available-date: 10/21/2024;
    name: Xia; bill-rate: $58.00 Per Hour; available-date: 11/04/2024;
    name: Wei; bill-rate: $55.00 Per Hour; available-date: 10/21/2024;
    name: Feng; bill-rate: $53.00 Per Hour; available-date: 11/18/2024;
    name: Zhao; bill-rate: $50.00 Per Hour; available-date: 11/11/2024;
    
    Show me all candidates with Bill Rate less than $55.
    """,
    stream=True,
)
