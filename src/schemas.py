from enum import Enum

from pydantic import BaseModel


class Genre(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    adult: bool
    backdrop_path: str
    genre_ids: list[int]
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: str
    title: str
    video: bool
    vote_average: float
    vote_count: int


class ProductionCompany(BaseModel):
    id: int
    logo_path: str
    name: str
    origin_country: str


class ProductionCountry(BaseModel):
    iso_3166_1: str
    name: str


class SpokenLanguage(BaseModel):
    english_name: str
    iso_639_1: str
    name: str


class BelongsToCollection(BaseModel):
    id: int
    name: str
    poster_path: str
    backdrop_path: str


class CountryCode(Enum):
    US = "US"
    GB = "GB"
    CA = "CA"
    FR = "FR"
    DE = "DE"
    JP = "JP"
    IN = "IN"
    CN = "CN"
    KR = "KR"
    IT = "IT"


class SortBy(str, Enum):
    origional_title_asc = "original_title.asc"
    origional_title_desc = "original_title.desc"
    popularity_desc = "popularity.desc"
    popularity_asc = "popularity.asc"
    revenue_desc = "revenue.desc"
    revenue_asc = "revenue.asc"
    primary_release_date_asc = "primary_release_date.asc"
    primary_release_date_desc = "primary_release_date.desc"
    title_asc = "title.asc"
    title_desc = "title.desc"
    vote_average_desc = "vote_average.desc"
    vote_average_asc = "vote_average.asc"
    vote_count_desc = "vote_count.desc"
    vote_count_asc = "vote_count.asc"
