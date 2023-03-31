from .exceptions import *
from datetime import datetime


def data_processing(data: object) -> None:
    actually_year = datetime.now()
    world_cup_quantities = []
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    validated_year_cup = []
    for year in range(1930, actually_year.year, 4):
        if int(data["first_cup"][:4]) == year:
            validated_year_cup.append(year)
    if len(validated_year_cup) == 0:
        raise InvalidYearCupError("there was no world cup this year")
    for year in range(int(data["first_cup"][:4]), actually_year.year, 4):
        world_cup_quantities.append(year)
    if data["titles"] > len(world_cup_quantities):
        raise ImpossibleTitlesError(
            ("impossible to have more titles than disputed cups")
        )
