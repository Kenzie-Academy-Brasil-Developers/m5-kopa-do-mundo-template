from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime, timedelta


def data_processing(country: dict):
    if country["titles"] < 0:
        raise NegativeTitlesError()
    
    first = country["first_cup"]
    first_formated = datetime.strptime(first, "%Y-%m-%d")
    year = first_formated.year
    first_world_cup = 1930
    years_since = year - first_world_cup
    
    if year < first_world_cup or years_since % 4 != 0:
        raise InvalidYearCupError()
    
    editions_of_country = (2022 - year) // 4 + 1
    if country["titles"] > editions_of_country:
        raise ImpossibleTitlesError()
    