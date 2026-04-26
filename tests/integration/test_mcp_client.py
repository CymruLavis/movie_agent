import pytest
import pytest_asyncio
from dotenv import load_dotenv
from fastmcp.client import Client
from fastmcp.client.client import CallToolResult
from mcp.types import Tool

from src.mcp.server import mcp
from src.mcp.tools.schemas import (
    DiscoverMovieInput,
    DiscoverMovieOutput,
    GenreMappingInput,
    GenreMappingOutput,
    MovieDetailsInput,
    MovieDetailsOutput,
    PopularMoviesInput,
    PopularMoviesOutput,
)
from src.schemas import Genre, Movie

load_dotenv()


@pytest.fixture
def client_url():
    return "http://localhost:3000/mcp"


@pytest_asyncio.fixture
async def client_session():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client


@pytest.mark.asyncio
async def test_get_tool_list(client_session):
    tools = await client_session.list_tools()
    tool_names = [
        t.annotations.title
        for tool in tools
        for t in [Tool.model_validate(tool)]
        if t.annotations
    ]
    print(f"There are {len(tool_names)} in this MCP Server")
    print(tool_names)
    assert len(tool_names) == 4


@pytest.mark.asyncio
async def test_movie_details_tool(client_session):
    input_params = MovieDetailsInput(movie_id=52156)
    result = await client_session.call_tool(
        "movie_details_tool", {"params": input_params.model_dump()}
    )
    assert isinstance(result, CallToolResult)
    my_results = [
        MovieDetailsOutput.model_validate_json(r.text)
        for r in result.content
        if r.type == "text"
    ]
    assert len(my_results) == 1
    my_result = my_results[0]
    print(my_result.title)
    print(my_result.genres)
    print(my_result.overview)


@pytest.mark.asyncio
async def test_list_popular_movies_tool(client_session):
    input_params = PopularMoviesInput()
    result = await client_session.call_tool(
        "list_popular_movies_tool", {"params": input_params.model_dump()}
    )
    assert isinstance(result, CallToolResult)
    my_results = [
        PopularMoviesOutput.model_validate_json(r.text)
        for r in result.content
        if r.type == "text"
    ]
    assert len(my_results) == 1
    my_result = my_results[0]
    assert all(isinstance(r, Movie) for r in my_result.results)
    example_result = my_result.results[0]
    print(example_result.title)
    print(example_result.release_date)
    print(example_result.genre_ids)
    print(example_result.vote_average)
    print(example_result.overview)


@pytest.mark.asyncio
async def test_genre_map_tool(client_session):
    input_params = GenreMappingInput()
    result = await client_session.call_tool(
        "genre_map_tool", {"params": input_params.model_dump()}
    )
    assert isinstance(result, CallToolResult)
    my_results = [
        GenreMappingOutput.model_validate_json(r.text)
        for r in result.content
        if r.type == "text"
    ]
    assert len(my_results) == 1
    my_result = my_results[0]
    assert all(isinstance(r, Genre) for r in my_result.genres)
    example_result = my_result.genres[0]
    print(f"ID: {example_result.id}, Genre: {example_result.name}")


@pytest.mark.asyncio
async def test_discover_movies_tool(client_session):
    input_params = DiscoverMovieInput(include_adult=True, primary_release_year=2024)
    result = await client_session.call_tool(
        "discover_movies_tool", {"params": input_params.model_dump()}
    )
    assert isinstance(result, CallToolResult)
    my_results = [
        DiscoverMovieOutput.model_validate_json(r.text)
        for r in result.content
        if r.type == "text"
    ]
    assert len(my_results) == 1
    my_result = my_results[0]
    assert all(isinstance(r, Movie) for r in my_result.results)
    example_result = my_result.results[0]
    print(example_result.title)
    print(example_result.release_date)
    print(example_result.genre_ids)
    print(example_result.vote_average)
    print(example_result.overview)
