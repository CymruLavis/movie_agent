from src.clients.tmdb import TMDBClient
from src.mcp.tools.schemas import PopularMoviesInput, PopularMoviesOutput


async def list_popular_movies(
    client: TMDBClient, input_params: PopularMoviesInput
) -> PopularMoviesOutput:
    """ """
    return PopularMoviesOutput.model_validate(
        client.list_popular_movies(params=input_params)
    )
