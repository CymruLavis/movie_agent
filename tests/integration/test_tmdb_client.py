import httpx
import pytest
from dotenv import load_dotenv

from src.clients.tmdb import TMDBClient
from src.config import TMDBConfig
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

"""
Test Plan
Testing all endpoints of TMDBClient
Mock
get_genre_mapping
get_movie_details
list_popular_movies
discover_movie

One Real test
get_genre_mapping
"""
load_dotenv()


@pytest.fixture
def get_config():
    return TMDBConfig().load()


@pytest.fixture
def get_client(get_config):
    return TMDBClient(config=get_config)


@pytest.fixture
def get_discover_movie_input():
    return DiscoverMovieInput()


@pytest.fixture
def get_list_popular_movie_input():
    return PopularMoviesInput()


@pytest.fixture
def get_move_details_input():
    return MovieDetailsInput(movie_id=502356)


@pytest.fixture
def get_genre_mapping():
    return GenreMappingInput()


def test_client_connection(get_client):
    client = get_client
    result = httpx.get(url=client._base_url, headers=client._build_headers())
    assert result.status_code == 204


@pytest.mark.asyncio
async def test_genre_mapping(get_client, get_genre_mapping):
    result = await get_client.get_genre_mapping(input_params=get_genre_mapping)
    assert isinstance(result, GenreMappingOutput)


@pytest.mark.asyncio
async def test_movie_details(get_client, get_move_details_input):
    result = await get_client.get_movie_details(params=get_move_details_input)
    assert MovieDetailsOutput.model_validate(result)


@pytest.mark.asyncio
async def test_list_popoular_movies(get_client, get_list_popular_movie_input):
    result = await get_client.list_popular_movies(params=get_list_popular_movie_input)
    assert PopularMoviesOutput.model_validate(result)


@pytest.mark.asyncio
async def test_discover_movies(get_client, get_discover_movie_input):
    result = await get_client.discover_movie(params=get_discover_movie_input)
    assert DiscoverMovieOutput.model_validate(result)
