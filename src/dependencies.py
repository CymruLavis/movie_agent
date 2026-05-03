from src.agent.agent import MovieAgent
from src.clients.openai import OpenAIClient
from src.clients.tmdb import TMDBClient
from src.config import OpenAIConfig, TMDBConfig


def get_tmdb_config():
    return TMDBConfig.load()


def get_tmdb_client():
    return TMDBClient(get_tmdb_config())


def get_openai_config():
    return OpenAIConfig.load()


def get_openai_client():
    return OpenAIClient(get_openai_config())


def get_openai_model():
    client = get_openai_client()
    return client.get_model()


def get_agent():
    from src.mcp.server import mcp

    return MovieAgent(get_openai_model(), mcp=mcp)
