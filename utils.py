from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(data):
    titles = data.get("titles")
    first_cup = int(data.get("first_cup")[:4])

    if titles < 0:
        raise NegativeTitlesError()

    if first_cup < 1930 or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError()

    max_possible_titles = (2024 - first_cup)//4+1
    if titles > max_possible_titles:
        raise ImpossibleTitlesError()

    return "Data processada com sucesso"
