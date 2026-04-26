from src.dependencies import get_tmdb_client
from src.mcp.tools.schemas import DiscoverMovieInput, DiscoverMovieOutput


async def discover_movies(params: DiscoverMovieInput) -> DiscoverMovieOutput:
    client = get_tmdb_client()
    return DiscoverMovieOutput.model_validate(
        await client.discover_movie(params=params)
    )
