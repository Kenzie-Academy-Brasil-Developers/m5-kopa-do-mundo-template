from datetime import datetime as dt

from exceptions import *


def data_processing(data: dict):

    first_world_cup = dt(1930, 1, 1)
    last_world_cup = dt(2022, 1, 1)

    date_first_cup = dt.strptime(data["first_cup"], "%Y-%m-%d")

    all_years_interval_last_first_cup = date_first_cup.year - first_world_cup.year
    all_cup_interval = (last_world_cup.year - date_first_cup.year) // 4

    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if date_first_cup.year < first_world_cup.year or all_years_interval_last_first_cup % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if data["titles"] > all_cup_interval:
        raise ImpossibleTitlesError(
            "impossible to have more titles than disputed cups")
