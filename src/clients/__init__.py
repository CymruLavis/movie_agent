from src.clients.tmdb import TMDBClient
from src.dependencies import get_tmdb_config


class Clients:
    def __init__(self):
        self.tmdb: TMDBClient = TMDBClient(get_tmdb_config())


clients = Clients()
