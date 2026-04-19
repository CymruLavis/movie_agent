from src.clients import clients
from src.mcp.tools.schemas import PopularMoviesInput, PopularMoviesOutput


async def list_popular_movies(params: PopularMoviesInput) -> PopularMoviesOutput:
    return PopularMoviesOutput.model_validate(
        clients.tmdb.list_popular_movies(params=params)
    )
