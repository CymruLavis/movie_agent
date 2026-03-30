from src.clients.tmdb import TMDBClient
from src.mcp.tools.schemas import PopularMoviesInput, PopularMoviesOutput
from fastmcp import FastMCP
from mcp.types import ToolAnnotations

def create_list_popular_movies_tool() -> FastMCP:
    mcp = FastMCP(name="list_popular_movies_tool", mask_error_details=True)

    @mcp.tool(
        annotations=ToolAnnotations(
            title="List Popular Movies",
            readOnlyHint=True,
            destructiveHint=False,
            idempotentHint=True,
            openWorldHint=False,
        )
    )
    async def list_popular_movies(
        client: TMDBClient, input_params: PopularMoviesInput
    ) -> PopularMoviesOutput:
        """ """
        return await client.list_popular_movies(params=input_params)

    return mcp