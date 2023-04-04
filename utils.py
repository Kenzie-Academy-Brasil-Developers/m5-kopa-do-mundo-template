from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime, timedelta


def data_processing(data: dict):
    years_cup = list(range(1930, datetime.now().year + 1, 4))

    first_year_cup = datetime.strptime(data["first_cup"], "%Y-%m-%d")

    max_cup = list(range(first_year_cup.year, datetime.now().year + 1, 4))

    if data["titles"] < 0:
        raise NegativeTitlesError
    
    if years_cup.count(first_year_cup.year) == 0:
        raise InvalidYearCupError
    
    if data['titles'] > len(max_cup):
        raise ImpossibleTitlesError
