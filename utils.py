from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime

def data_processing(select_info: dict):
    if select_info["titles"] < 0:
        raise NegativeTitlesError

    initial_year = 1930
    interval = 4
    end_year = 2018

    current_year = initial_year
    years_cup = []

    while current_year <= end_year:
        years_cup.append(current_year)
        current_year += interval

    first_cup_year = datetime.strptime(select_info["first_cup"], "%Y-%m-%d").year
    if first_cup_year not in years_cup:
        raise InvalidYearCupError

    if select_info["titles"] not in years_cup:
        raise ImpossibleTitlesError
 

