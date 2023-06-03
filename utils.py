from datetime import datetime, timedelta
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data):
    titles = data["titles"]
    first_cup = data["first_cup"]

    if titles < 0:
        raise NegativeTitlesError()

    first_cup_year = datetime.strptime(first_cup, "%Y-%m-%d").year
    current_year = datetime.now().year
    if (
        first_cup_year < 1930
        or first_cup_year > current_year
        or (first_cup_year - 1930) % 4 != 0
    ):
        raise InvalidYearCupError()

    max_possible_titles = (current_year - first_cup_year) / 4
    if titles > max_possible_titles:
        raise ImpossibleTitlesError()

    return "Data processing successful"
