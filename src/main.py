import asyncio

from rich.console import Console

from src.dependencies import get_agent


async def main():
    agent = get_agent()
    console = Console()
    console.print("Welcome to the Movie Reccomendation Agent")
    response = agent.run("What movie should i watch")
    console.print(response)


if __name__ == "__main__":
    asyncio.run(main())
