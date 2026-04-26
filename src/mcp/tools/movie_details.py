from src.dependencies import get_tmdb_client
from src.mcp.tools.schemas import MovieDetailsInput, MovieDetailsOutput


async def get_movie_details(params: MovieDetailsInput) -> MovieDetailsOutput:
    client = get_tmdb_client()
    return MovieDetailsOutput.model_validate(
        await client.get_movie_details(params=params)
    )
