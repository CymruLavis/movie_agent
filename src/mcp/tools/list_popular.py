from src.dependencies import get_tmdb_client
from src.mcp.tools.schemas import PopularMoviesInput, PopularMoviesOutput


async def list_popular_movies(params: PopularMoviesInput) -> PopularMoviesOutput:
    client = get_tmdb_client()
    return PopularMoviesOutput.model_validate(
        await client.list_popular_movies(params=params)
    )
