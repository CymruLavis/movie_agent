from src.clients.tmdb import TMDBClient
from src.mcp.tools.schemas import MovieDetailsInput, MovieDetailsOutput


async def get_movie_details(
    client: TMDBClient, input_params: MovieDetailsInput
) -> MovieDetailsOutput:
    """ """
    return MovieDetailsOutput.model_validate(
        await client.get_movie_details(params=input_params)
    )
