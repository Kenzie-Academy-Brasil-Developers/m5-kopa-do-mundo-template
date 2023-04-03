from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data):

    titles = data["titles"]
    first_cup = int(data["first_cup"][:4])
    current_year = 2023

    if type(data) is not dict:
        raise TypeError({"error": "data must be a dict"})

    if titles < 0:
        raise NegativeTitlesError({"error": "titles cannot be negative"})

    if first_cup < 1930 or first_cup > current_year or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError({"error": "there was no world cup this year"})

    max_titles = (current_year - first_cup) // 4
    if titles > max_titles:
        raise ImpossibleTitlesError(
            {"error": "impossible to have more titles than disputed cups"}
        )

    return data
