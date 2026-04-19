# from contextlib import asynccontextmanager
# from dataclasses import dataclass

from fastmcp import FastMCP
from mcp.types import ToolAnnotations

# from openai import AsyncOpenAI
# from src.clients.tmdb import TMDBClient
# from src.config import TMDBConfig
from src.mcp.tools.discover_movie import discover_movies
from src.mcp.tools.genre_map import get_genre_map
from src.mcp.tools.list_popular import list_popular_movies
from src.mcp.tools.movie_details import get_movie_details
from src.mcp.tools.schemas import (
    DiscoverMovieInput,
    DiscoverMovieOutput,
    GenreMappingInput,
    MovieDetailsInput,
    MovieDetailsOutput,
    PopularMoviesInput,
    PopularMoviesOutput,
)

# @dataclass
# class MCPContext:
#     tmdb_client: TMDBClient


# @asynccontextmanager
# async def app_lifespan(server: FastMCP):

#     tmdb_config = TMDBConfig.load()

#     tmdb_client = TMDBClient(config=tmdb_config)
#     openai_client = AsyncOpenAI()

#     try:
#         yield MCPContext(tmdb_client=tmdb_client)
#     finally:
#         await openai_client.close()


mcp = FastMCP(name="MovieAgentMCP")


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Movie Details",
        readOnlyHint=True,
    )
)
async def movie_details_tool(params: MovieDetailsInput) -> MovieDetailsOutput:
    """
    <usecase>
    Extract further, fine grain details about a specific movie to answer deeper questions
    </usecase>

    <instructions>
    Use this tool when the user is trying to find out more about a particualr movie.
    The input will require the movies tmdb id
    </instructions>
    """
    return await get_movie_details(params=params)


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Popular Movies",
        readOnlyHint=True,
    )
)
async def list_popular_movies_tool(params: PopularMoviesInput) -> PopularMoviesOutput:
    """
    <usecase>
    Provide a list of currently popular movies when the user doesn't know what they want
    </usecase>

    <instructions>
    Use this tool when the user doesn't give any helpful filters to narrow down the movie search with
    </instructions>
    """
    return await list_popular_movies(params=params)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Discover Movies",
        readOnlyHint=True,
    )
)
async def discover_movies_tool(params: DiscoverMovieInput) -> DiscoverMovieOutput:
    """
    <usecase>
    Search for a list of movies to match your filters. Returns a list
    </usecase>

    <instructions>
    Use this tool when given specific criteria from the user to filter potential movies to (i.e. genre, lead actor, director, runtime,  etc)
    </instructions>
    """
    return await discover_movies(params=params)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Genre Map",
        readOnlyHint=True,
    )
)
async def genre_map_tool(params: GenreMappingInput):
    """
    <usecase>
    Return the id:name mapping for the genres of TMDB.
    </usecase>

    <instructions>
    Use this as an intermediate step when the user is asking for movies based on genres and the ID is needed for filters in other tools.
    The input is the language code in which you are working in. The language code is a 2 character ISO 639-1 code (i.e en=English, fr=French, de=German)
    </instructions>
    """
    return await get_genre_map(params=params)
