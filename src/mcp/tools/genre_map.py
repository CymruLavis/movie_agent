from src.clients import clients
from src.mcp.tools.schemas import GenreMappingInput, GenreMappingOutput


async def get_genre_map(params: GenreMappingInput) -> GenreMappingOutput:
    return GenreMappingOutput.model_validate(
        clients.tmdb.get_genre_mapping(params=params)
    )
