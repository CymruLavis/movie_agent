from fastmcp import FastMCP
from mcp.types import ToolAnnotations

from src.mcp.tools.discover_movie import discover_movies
from src.mcp.tools.genre_map import get_genre_map
from src.mcp.tools.list_popular import list_popular_movies
from src.mcp.tools.movie_details import get_movie_details
from src.mcp.tools.schemas import (
    DiscoverMovieInput,
    DiscoverMovieOutput,
    GenreMappingInput,
    GenreMappingOutput,
    MovieDetailsInput,
    MovieDetailsOutput,
    PopularMoviesInput,
    PopularMoviesOutput,
)

mcp = FastMCP(name="MovieAgentMCP")


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Movie Details",
        readOnlyHint=True,
    ),
    output_schema=MovieDetailsOutput.model_json_schema(),
)
async def movie_details_tool(params: MovieDetailsInput) -> MovieDetailsOutput:
    """
    <usecase>
    Extract further, fine grain details about a specific movie to answer deeper questions
    </usecase>

    <instructions>
    Use this tool when the user is trying to find out more about a particualr movie.
    The input will require the movies tmdb id
    </instructions>

    <input_schema>
    {
        "params":
        {
            movie_id: int = Field(description="The ID of the movie to retrieve details for.")
            append_to_response: Optional[str] = Field(
                default=None,
                description="comma separated list of endpoints within this namespace, 20 items max, to append to the result. See https://developers.themoviedb.org/3/getting-started/append-to-response for more details.",
            )
            language: str = Field(
                default="en-US",
                description="The language to return results in. the code is constructed with an ISO 639-1 language code and an ISO 3166-1 country code, joined by a hyphen. (e.g. en-US). If the specified language doesn't exist, it will default to English (en-US).",
            )

        }
    }
    </input_schema>
    """
    return await get_movie_details(params=params)


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Popular Movies",
        readOnlyHint=True,
    ),
    output_schema=PopularMoviesOutput.model_json_schema(),
)
async def list_popular_movies_tool(params: PopularMoviesInput) -> PopularMoviesOutput:
    """
    <usecase>
    Provide a list of currently popular movies when the user doesn't know what they want
    </usecase>

    <instructions>
    Use this tool when the user doesn't give any helpful filters to narrow down the movie search with
    </instructions>

    <input_schema>
    {
        "params": {
            language: str = Field(
            default="en-US",
            description="The language to return results in. the code is constructed with an ISO 639-1 language code and an ISO 3166-1 country code, joined by a hyphen. (e.g. en-US). If the specified language doesn't exist, it will default to English (en-US).",
            )
            page: int = Field(default=1, description="The page of results to return.")
            region: Optional[str] = Field(
                default=None,
                description="Specify a ISO 3166-1 code to filter regional results. Must be uppercase. (e.g. US)",
            )
        }
    }
    </input_schema>
    """
    return await list_popular_movies(params=params)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Discover Movies",
        readOnlyHint=True,
    ),
    output_schema=DiscoverMovieOutput.model_json_schema(),
)
async def discover_movies_tool(params: DiscoverMovieInput) -> DiscoverMovieOutput:
    """
    <usecase>
    Search for a list of movies to match your filters. Returns a list
    </usecase>

    <instructions>
    Use this tool when given specific criteria from the user to filter potential movies to (i.e. genre, lead actor, director, runtime,  etc)
    </instructions>

    <input_schema>
    {
        "params": {
        certification: Optional[str] = Field(
        default=None, description="Filter by certification rating (use with region)"
    )
    certification_gte: Optional[str] = Field(
        default=None,
        alias="certification.gte",
        description="Filter certifications greater than or equal (use with region)",
    )
    certification_lte: Optional[str] = Field(
        default=None,
        alias="certification.lte",
        description="Filter certifications less than or equal (use with region)",
    )
    certification_country: Optional[str] = Field(
        default=None, description="Country for certification filters"
    )

    include_adult: bool = Field(
        default=False, description="Include adult (NSFW) content"
    )
    include_video: bool = Field(default=False, description="Include videos")

    language: str = Field(
        default="en-US", description="Language for results (ISO format)"
    )
    page: int = Field(default=1, description="Page number for pagination")

    primary_release_year: Optional[int] = Field(
        default=None, description="Filter by primary release year"
    )
    primary_release_date_gte: Optional[datetime] = Field(
        default=None,
        alias="primary_release_date.gte",
        description="Primary release date greater than or equal",
    )
    primary_release_date_lte: Optional[datetime] = Field(
        default=None,
        alias="primary_release_date.lte",
        description="Primary release date less than or equal",
    )

    region: Optional[str] = Field(
        default=None, description="Filter by region (ISO 3166-1 code)"
    )
    release_date_gte: Optional[datetime] = Field(
        default=None,
        alias="release_date.gte",
        description="Release date greater than or equal",
    )
    release_date_lte: Optional[datetime] = Field(
        default=None,
        alias="release_date.lte",
        description="Release date less than or equal",
    )

    sort_by: SortBy = Field(
        default=SortBy.popularity_desc,
        description="Sort results by field and direction",
    )

    vote_average_gte: Optional[float] = Field(
        default=None, alias="vote_average.gte", description="Minimum vote average"
    )
    vote_average_lte: Optional[float] = Field(
        default=None, alias="vote_average.lte", description="Maximum vote average"
    )
    vote_count_gte: Optional[float] = Field(
        default=None, alias="vote_count.gte", description="Minimum vote count"
    )
    vote_count_lte: Optional[float] = Field(
        default=None, alias="vote_count.lte", description="Maximum vote count"
    )

    watch_region: Optional[str] = Field(
        default=None, description="Region for watch provider filters"
    )

    with_cast: Optional[str] = Field(
        default=None, description="Filter by cast (comma=AND, pipe=OR)"
    )
    with_companies: Optional[str] = Field(
        default=None, description="Filter by production companies (comma=AND, pipe=OR)"
    )
    with_crew: Optional[str] = Field(
        default=None, description="Filter by crew (comma=AND, pipe=OR)"
    )
    with_genres: Optional[str] = Field(
        default=None, description="Filter by genres (comma=AND, pipe=OR)"
    )
    with_keywords: Optional[str] = Field(
        default=None, description="Filter by keywords (comma=AND, pipe=OR)"
    )
    with_origin_country: Optional[str] = Field(
        default=None, description="Filter by origin country"
    )
    with_original_language: Optional[str] = Field(
        default=None, description="Filter by original language"
    )
    with_people: Optional[str] = Field(
        default=None, description="Filter by people (comma=AND, pipe=OR)"
    )

    with_release_type: Optional[str] = Field(
        default=None,
        description="Release types [1-6], comma=AND, pipe=OR (use with region)",
    )

    with_runtime_gte: Optional[int] = Field(
        default=None, alias="with_runtime.gte", description="Minimum runtime (minutes)"
    )
    with_runtime_lte: Optional[int] = Field(
        default=None, alias="with_runtime.lte", description="Maximum runtime (minutes)"
    )

    with_watch_monetization_types: Optional[str] = Field(
        default=None, description="Monetization types [flatrate, free, ads, rent, buy]"
    )
    with_watch_providers: Optional[str] = Field(
        default=None, description="Watch providers (use with watch_region)"
    )

    without_companies: Optional[str] = Field(
        default=None, description="Exclude production companies"
    )
    without_genres: Optional[str] = Field(default=None, description="Exclude genres")
    without_keywords: Optional[str] = Field(
        default=None, description="Exclude keywords"
    )
    without_watch_providers: Optional[str] = Field(
        default=None, description="Exclude watch providers"
    )

    year: Optional[int] = Field(default=None, description="Filter by release year")
    }
    }
    </input_schema>
    """
    return await discover_movies(params=params)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Genre Map",
        readOnlyHint=True,
    ),
    output_schema=GenreMappingOutput.model_json_schema(),
)
async def genre_map_tool(params: GenreMappingInput) -> GenreMappingOutput:
    """
    <usecase>
    Return the id:name mapping for the genres of TMDB.
    </usecase>

    <instructions>
    Use this as an intermediate step when the user is asking for movies based on genres and the ID is needed for filters in other tools.
    The input is the language code in which you are working in. The language code is a 2 character ISO 639-1 code (i.e en=English, fr=French, de=German)
    </instructions>

    <input_schema>
    {
        "params": {language: str = "en"}
    }
    </input_schema>
    """
    return await get_genre_map(params=params)
