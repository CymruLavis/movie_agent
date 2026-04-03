from contextlib import asynccontextmanager
from dataclasses import dataclass

from fastmcp import FastMCP
from mcp.types import ToolAnnotations
from openai import AsyncOpenAI

from src.clients.tmdb import TMDBClient
from src.config import TMDBConfig
from src.mcp.tools.discover_movie import discover_movies
from src.mcp.tools.list_popular import list_popular_movies
from src.mcp.tools.movie_details import get_movie_details
from src.mcp.tools.schemas import (
    DiscoverMovieInput,
    DiscoverMovieOutput,
    MovieDetailsInput,
    MovieDetailsOutput,
    PopularMoviesInput,
    PopularMoviesOutput,
)


@dataclass
class MCPContext:
    tmdb_client: TMDBClient


@asynccontextmanager
async def app_lifespan(server: FastMCP):

    tmdb_config = TMDBConfig.load()

    tmdb_client = TMDBClient(config=tmdb_config)
    openai_client = AsyncOpenAI()

    try:
        yield MCPContext(tmdb_client=tmdb_client)
    finally:
        await openai_client.close()


mcp = FastMCP(name="MovieAgentMCP", mask_error_details=True, lifespan=app_lifespan)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Movie Details",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
async def movie_details_tool(
    context: MCPContext, input_params: MovieDetailsInput
) -> MovieDetailsOutput:
    """ """
    return await get_movie_details(
        client=context.tmdb_client, input_params=input_params
    )


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Popular Movies",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
async def list_popular_movies_tool(
    context: MCPContext, input_params: PopularMoviesInput
) -> PopularMoviesOutput:
    """ """
    return await list_popular_movies(
        client=context.tmdb_client, input_params=input_params
    )


@mcp.tool(
    annotations=ToolAnnotations(
        title="Discover Movies",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
async def discover_movies_tool(
    context: MCPContext, input_params: DiscoverMovieInput
) -> DiscoverMovieOutput:
    """"""
    return await discover_movies(client=context.tmdb_client, input_params=input_params)
