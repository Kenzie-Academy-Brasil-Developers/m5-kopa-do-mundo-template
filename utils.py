from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(selection_info):
    titles = selection_info.get("titles")
    first_cup = selection_info.get("first_cup")

    if titles is not None and titles < 0:
        raise NegativeTitlesError()

    if first_cup is not None:
        first_cup_year = int(first_cup.split("-")[0])

        if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
            raise InvalidYearCupError()

        if titles is not None and titles > ((2022 - first_cup_year) // 4) + 1:
            raise ImpossibleTitlesError()
