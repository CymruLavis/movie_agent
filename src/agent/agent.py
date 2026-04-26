from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.toolsets.fastmcp import FastMCPToolset

from src.mcp.server import mcp

load_dotenv()


class MovieAgent:
    def __init__(self, openai_client) -> None:
        self.openai_client = openai_client
        self.agent = Agent(model=self.openai_client, toolsets=[FastMCPToolset(mcp)])
        self.system_prompt: str = "temp prompt"

    async def run(self, input_prompt: str):
        async with self.agent.run_stream(user_prompt=input_prompt) as result:
            yield result
