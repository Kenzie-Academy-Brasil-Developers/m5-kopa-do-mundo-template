from exceptions import NegativeTitlesError
from exceptions import ImpossibleTitlesError
from exceptions import InvalidYearCupError

def data_processing(dict: dict):
    first_cup = 1930
    last_cup = 2022
    if dict["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    if int(dict["first_cup"][0:4]) < first_cup or (int(dict["first_cup"][0:4]) - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")
    if dict["titles"] > (last_cup - int(dict["first_cup"][0:4])) / 4:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
    pass