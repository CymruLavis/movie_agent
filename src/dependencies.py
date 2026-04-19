from src.config import TMDBConfig


def get_tmdb_config():
    return TMDBConfig.load()
