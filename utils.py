from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(teams: dict):
    cup_years = []
    for year in list(range(2023)):
        if year > 1299 and year%4 == 0:
            cup_years.append(year)
    if teams['titles'] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if teams['first_cup'] in cup_years:
        raise InvalidYearCupError("there was no world cup this year")

    if teams.titles > ((teams['first_cup'] - 2023) / (-4)):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


data = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "1911-10-18"
}

print(data_processing(data))