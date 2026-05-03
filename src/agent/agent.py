from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.toolsets.fastmcp import FastMCPToolset
from fastmcp import FastMCP
from typing import Any
from collections.abc import Sequence
from pydantic_ai.messages import ModelResponse


load_dotenv()


class MovieAgent:
    def __init__(self, openai_client, mcp: FastMCP[Any]) -> None:
        self.openai_client = openai_client
        self.agent = Agent(model=self.openai_client, toolsets=[FastMCPToolset(mcp)], system_prompt=self.get_system_prompt())

    def get_system_prompt(self) -> str:
        with open("src/agent/system_prompt.txt", "r") as file:
            return file.read()

    async def run(self, input_prompt: str, history: Sequence[ModelResponse]):
        async with self.agent.run_stream(user_prompt=input_prompt, message_history=history) as events:
            async for event in events.stream_responses():
                yield event