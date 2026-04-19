from src.clients import clients
from src.mcp.tools.schemas import DiscoverMovieInput, DiscoverMovieOutput


async def discover_movies(params: DiscoverMovieInput) -> DiscoverMovieOutput:
    return DiscoverMovieOutput.model_validate(
        await clients.tmdb.discover_movie(params=params)
    )
