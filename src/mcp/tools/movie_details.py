from src.clients import clients
from src.mcp.tools.schemas import MovieDetailsInput, MovieDetailsOutput


async def get_movie_details(params: MovieDetailsInput) -> MovieDetailsOutput:
    return MovieDetailsOutput.model_validate(
        await clients.tmdb.get_movie_details(params=params)
    )
