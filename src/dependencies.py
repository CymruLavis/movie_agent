from src.clients.tmdb import TMDBClient
from src.config import TMDBConfig


def get_tmdb_config():
    return TMDBConfig.load()


def get_tmdb_client():
    return TMDBClient(get_tmdb_config())
