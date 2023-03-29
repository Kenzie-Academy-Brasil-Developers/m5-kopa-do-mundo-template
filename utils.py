from exceptions import NegativeTitlesError, ImpossibleTitlesError, InvalidYearCupError


def data_processing(data: dict):
    titles = data[titles]
    first_coup_rec = data[first_cup[:3]]
    first_cup_defined = 1930

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if first_coup_rec < first_cup_defined:
        raise InvalidYearCupError("there was no world cup this year")
    while first_coup_rec > first_cup_defined:
        first_coup_rec - 4
        if first_coup_rec < first_coup:
            raise InvalidYearCupError("there was no world cup this year")

    if (titles**4 % 4) != 0:
        raise InvalidYearCupError("there was no world cup this year")
    if (titles**4 + first_cup_defined) > 2022:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
