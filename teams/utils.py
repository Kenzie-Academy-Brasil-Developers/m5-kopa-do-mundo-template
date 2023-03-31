from datetime import datetime

from teams.exceptions import ImpossibleTitlesError, InvalidYearCupError
from teams.exceptions import NegativeTitlesError


def data_processing(infos_team):
    if infos_team["titles"] < 0:
        raise NegativeTitlesError()

    first_cup_year = int(infos_team["first_cup"][:4])
    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    number_titles = infos_team["titles"]
    now = datetime.now()
    ano = now.year
    possible_titles = (ano - first_cup_year) // 4

    if number_titles > possible_titles:
        raise ImpossibleTitlesError()
