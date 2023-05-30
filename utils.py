from exceptions import *
from datetime import datetime


def data_processing(info_selection: dict):
    # Verifica se titulos é negativo
    if info_selection["titles"] < 0:
        raise NegativeTitlesError
    # Transforma a data de string para date
    first_cup_date = datetime.strptime(info_selection["first_cup"], "%Y-%m-%d").date()
    # verifica se o ano é valido
    first_cup_year = first_cup_date.year
    if (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError
    # Verifica numero de copas
    current_year = datetime.now().year
    num_cups = (current_year - first_cup_year) // 4
    if info_selection["titles"] > num_cups:
        raise ImpossibleTitlesError
