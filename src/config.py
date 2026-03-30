from pydantic_settings import BaseSettings, SettingsConfigDict


class TMDBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TMDB_")

    API_KEY: str
    API_READ_ACCESS_TOKEN: str
    BASE_URL: str = "https://api.themoviedb.org/3"
