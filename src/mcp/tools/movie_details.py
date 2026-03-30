from src.clients.tmdb import TMDBClient
from src.mcp.tools.schemas import MovieDetailsInput, MovieDetailsOutput
from fastmcp import FastMCP
from mcp.types import ToolAnnotations

def create_movie_details_tool() -> FastMCP:
    mcp = FastMCP(name="movie_details_tool", mask_error_details=True)

    @mcp.tool(
        annotations=ToolAnnotations(
            title="Get Movie Details",
            readOnlyHint=True,
            destructiveHint=False,
            idempotentHint=True,
            openWorldHint=False,
        )
    )
    async def get_movie_details(
        client: TMDBClient, input_params: MovieDetailsInput
    ) -> MovieDetailsOutput:
        """ """
        return await client.get_movie_details(params=input_params)

    return mcp