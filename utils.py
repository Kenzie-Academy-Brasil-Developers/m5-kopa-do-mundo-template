from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime as dt


def data_processing(data):

    first_cup = dt(1930, 1, 1).year
    info_cup = dt.strptime(data['first_cup'], '%Y-%m-%d').year
    act_year = dt.now().year
    total_titles = (first_cup - data['titles'])

    if data['titles'] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if (info_cup - first_cup) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if (total_titles < first_cup):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
