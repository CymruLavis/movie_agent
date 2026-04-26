from src.dependencies import get_tmdb_client
from src.mcp.tools.schemas import GenreMappingInput, GenreMappingOutput


async def get_genre_map(params: GenreMappingInput) -> GenreMappingOutput:
    client = get_tmdb_client()
    return GenreMappingOutput.model_validate(
        await client.get_genre_mapping(params=params)
    )
