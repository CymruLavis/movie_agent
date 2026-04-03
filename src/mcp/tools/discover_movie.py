from src.clients.tmdb import TMDBClient
from src.mcp.tools.schemas import DiscoverMovieInput, DiscoverMovieOutput


async def discover_movies(
    input_params: DiscoverMovieInput, client: TMDBClient
) -> DiscoverMovieOutput:
    """
    Discover movies based on various criteria such as genre, release date, and ratings.
    """
    return DiscoverMovieOutput.model_validate(
        await client.discover_movie(params=input_params)
    )
