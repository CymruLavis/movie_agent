import httpx

from src.config import TMDBConfig
from src.mcp.tools.schemas import (
    DiscoverMovieInput,
    GenreMappingInput,
    GenreMappingOutput,
    MovieDetailsInput,
    PopularMoviesInput,
)


class TMDBClient:
    def __init__(self, config: TMDBConfig):
        self._api_key = config.API_KEY
        self._api_read_access_token = config.API_READ_ACCESS_TOKEN
        self._base_url = config.BASE_URL

    def _build_headers(self) -> dict:
        return {"Authorization": f"Bearer {self._api_read_access_token}"}

    def _build_url(self, endpoint: str) -> str:
        return f"{self._base_url}/{endpoint}"

    async def _make_request(self, endpoint: str, params: dict) -> dict:
        async with httpx.AsyncClient() as client:
            url = self._build_url(endpoint)
            try:
                response = await client.get(
                    url=url, headers=self._build_headers(), params=params, timeout=10.0
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception(
                    f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
                )

    async def discover_movie(self, params: DiscoverMovieInput) -> dict:
        return await self._make_request(
            endpoint="discover/movie", params=params.model_dump(exclude_none=True)
        )

    async def list_popular_movies(self, params: PopularMoviesInput) -> dict:
        return await self._make_request(
            endpoint="movie/popular", params=params.model_dump(exclude_none=True)
        )

    async def get_movie_details(self, params: MovieDetailsInput) -> dict:
        return await self._make_request(
            endpoint="/movie/{movie_id}".format(movie_id=params.movie_id),
            params=params.model_dump(exclude_none=True),
        )

    async def get_genre_mapping(
        self, input_params: GenreMappingInput
    ) -> GenreMappingOutput:
        response_data = await self._make_request(
            endpoint="/genre/movie/list",
            params=input_params.model_dump(exclude_none=True),
        )
        return GenreMappingOutput.model_validate(response_data)
