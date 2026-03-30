from dataclasses import dataclass

from fastmcp import FastMCP
from contextlib import asynccontextmanager
from openai import AsyncOpenAI
from src.clients.tmdb import TMDBClient
from src.config import OpenAIConfig, TMDBConfig
from src.mcp.tools.discover_movie import create_discover_movies_tool
from src.mcp.tools.movie_details import create_movie_details_tool
from src.mcp.tools.list_popular import create_list_popular_movies_tool

@dataclass
class MCPContext:
    openai_client: AsyncOpenAI
    tmdb_client: TMDBClient


@asynccontextmanager
async def app_lifespan(server: FastMCP):

    tmdb_config = TMDBConfig.load()
    openai_config = OpenAIConfig.load()

    tmdb_client = TMDBClient(config=tmdb_config)
    openai_client = AsyncOpenAI()

    try:
        yield MCPContext(openai_client=openai_client, tmdb_client=tmdb_client)
    finally:
        await openai_client.close()


mcp = FastMCP(name="MovieAgentMCP", mask_error_details=True, lifespan=app_lifespan)

mcp.mount(create_discover_movies_tool())
mcp.mount(create_list_popular_movies_tool())
mcp.mount(create_movie_details_tool())