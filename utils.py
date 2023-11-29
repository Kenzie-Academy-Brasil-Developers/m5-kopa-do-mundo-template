from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data):
    from datetime import datetime

    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup = datetime.strptime(data["first_cup"], "%Y-%m-%d").year
    if first_cup % 4 != 2 or first_cup < 1930:
        raise InvalidYearCupError("there was no world cup this year")

    actual = datetime.now().year
    count = 0

    while first_cup <= actual:
        first_cup += 4
        count += 1

    if data["titles"] > count:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

    return data
