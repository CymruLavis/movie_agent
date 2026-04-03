from pydantic_settings import BaseSettings, SettingsConfigDict


class TMDBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TMDB_")

    API_KEY: str = "api_key_not_set"
    API_READ_ACCESS_TOKEN: str = "access_token_not_set"
    BASE_URL: str = "https://api.themoviedb.org/3"

    @classmethod
    def load(cls):
        return cls()


class OpenAIConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OPENAI_")

    API_KEY: str = "api_key_not_set"
    MODEL: str = "gpt-5-nano"

    @classmethod
    def load(cls):
        return cls()
