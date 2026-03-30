from src.config import TMDBConfig


async def get_tmdb_config():
    return TMDBConfig.load()
