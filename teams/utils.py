from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from datetime import datetime as dt


def data_processing(selection_infos):
    if selection_infos["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    today = dt.today()
    current_year = today.year
    cup_years = [1930]
    while cup_years[-1] < current_year:
        new_cup_year = cup_years[-1] + 4
        if new_cup_year > current_year:
            break
        cup_years.append(new_cup_year)

    first_cup_year = selection_infos["first_cup"].split("-")[0]
    valid_year = False
    for year in cup_years:
        if year == int(first_cup_year):
            valid_year = True
    if not valid_year:
        raise InvalidYearCupError("there was no world cup this year")

    possible_cup_participations = len(cup_years) - cup_years.index(int(first_cup_year))
    if (
        possible_cup_participations
        == 0 | possible_cup_participations
        < selection_infos["titles"]
    ):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


if __name__ == "__utils__":
    data_processing()
