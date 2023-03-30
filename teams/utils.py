from datetime import datetime as dt
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(teams: dict):
    cup_years = []
    for year in list(range(2023)):
        if year > 1929 and (year + 2) % 4 == 0:
            cup_years.append(year)

    if teams["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if not dt.strptime(teams["first_cup"], "%Y-%m-%d").year in cup_years:
        raise InvalidYearCupError("there was no world cup this year")

    if teams["titles"] > (
        (dt.strptime(teams["first_cup"], "%Y-%m-%d").year - 2023) / (-4)
    ):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

    return teams


data = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "1934-10-18",
}

print(data_processing(data))
