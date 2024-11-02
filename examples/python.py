from pathlib import Path

from phi.agent.python import PythonAgent
from phi.llm.azure_chat_model import AzureOpenAIChat    
from phi.file.local.csv import CsvFile

cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok=True, parents=True)

python_agent = PythonAgent(
    model=AzureOpenAIChat(id="gpt-4o"),
    base_dir=tmp,
    files=[
        CsvFile(
            path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            description="Contains information about movies from IMDB.",
        )
    ],
    markdown=True,
    pip_install=True,
    show_tool_calls=True,
)
python_agent.print_response(
    """I have six candidates in triple backquotes    
    name: Ming; bill-rate: $49.50 Per Hour; available-date: 11/18/2024;
    name: Li; bill-rate: $50.00 Per Hour; available-date: 10/21/2024;
    name: Xia; bill-rate: $58.00 name: Wei; bill-rate: $55.00 Per Hour; available-date: 10/21/2024;
    name: Feng; bill-rate: $53.00 Per Hour; available-date: 11/18/2024;
    name: Zhao; bill-rate: $50.00 Per Hour; available-date: 11/11/2024;
    
    Show me all candidates with Bill Rate less than $55.
    Use SQL-like thinking to analyze the data step by step.
    """
)


