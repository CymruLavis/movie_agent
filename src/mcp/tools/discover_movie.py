from src.mcp.tools.schemas import DiscoverMovieInput, DiscoverMovieResponse
from src.clients.tmdb import TMDBClient


async def discover_movie(
    input_params: DiscoverMovieInput, client: TMDBClient
) -> DiscoverMovieResponse:
    return await client.discover_movie(params=input_params)
