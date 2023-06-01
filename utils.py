from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime as dt


def is_world_cup_year(year: int) -> None:
    first_cup = int(year.split("-")[0])

    if first_cup < 1930 or first_cup % 4 - 2 != 0:
        raise InvalidYearCupError("there was no world cup this year")


def verify_titles(selection):
    first_cup_year = int(selection["first_cup"].split("-")[0])
    current_year = dt.now().year
    years_since_first_cup = current_year - first_cup_year

    if selection["titles"] > (years_since_first_cup // 4):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


def data_processing(selection: dict) -> None:
    if selection["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    is_world_cup_year(selection["first_cup"])
    verify_titles(selection)


data = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}


def main():
    print(data_processing(data))
    ...


if __name__ == "__main__":
    main()
