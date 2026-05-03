import asyncio

from pydantic_ai.capabilities import AgentNode
from rich.console import Console
from pydantic_ai.messages import ToolReturnPart, ModelResponse, TextPart
from pydantic_ai.agent import CallToolsNode, ModelRequestNode
from pydantic_graph.nodes import End
from src.dependencies import get_agent


async def main():
    agent = get_agent()
    console = Console()
    console.print("Welcome to the Movie Reccomendation Agent")
    converstaion_history = []
    while True:
        user_input = input("")
        if user_input in ["/exit", "/quit"]:
            console.print("Thank you for using the movie reccomendation agent!")
            break
        async for message in agent.run(input_prompt=user_input, history=converstaion_history):
            if message[1]:
                part = next((part for part in message[0].parts if isinstance(part, TextPart)))
                converstaion_history.append(message)
                console.print(part.content)

if __name__ == "__main__":
    asyncio.run(main())
