from teams.exceptions import NegativeTitlesError
from teams.exceptions import ImpossibleTitlesError
from teams.exceptions import InvalidYearCupError

def data_processing(**data):
    first_cup = 1930
    last_cup = 2022
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    if int(data["first_cup"][0:4]) < first_cup or (int(data["first_cup"][0:4]) - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")
    if data["titles"] > (last_cup - int(data["first_cup"][0:4])) / 4:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
    pass