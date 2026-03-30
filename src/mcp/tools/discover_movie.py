from src.mcp.tools.schemas import DiscoverMovieInput, DiscoverMovieResponse
from src.clients.tmdb import TMDBClient
from fastmcp import FastMCP
from mcp.types import ToolAnnotations


def create_discover_movies_tool() -> FastMCP:

    mcp = FastMCP(name="discover_movie_tool", mask_error_details=True)

    @mcp.tool(
        annotations=ToolAnnotations(
            title="Discover Movies",
            readOnlyHint=True,
            destructiveHint=False,
            idempotentHint=True,
            openWorldHint=False,
        )
    )
    async def discover_movie(
        input_params: DiscoverMovieInput, client: TMDBClient
    ) -> DiscoverMovieResponse:
        """
        Discover movies based on various criteria such as genre, release date, and ratings.
        """
        return await client.discover_movie(params=input_params)

    return mcp
