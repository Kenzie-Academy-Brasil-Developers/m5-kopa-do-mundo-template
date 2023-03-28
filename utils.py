from datetime import datetime
from exceptions import ImpossibleTitlesError, InvalidYearCupError 
from exceptions import NegativeTitlesError


def data_processing(infos_team):

    if infos_team["titles"] < 0:
        raise NegativeTitlesError()

    first_cup_year = int(infos_team["first_cup"][:4])
    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError()
    
    number_titles = infos_team["titles"]
    now = datetime.now()
    ano = now.year
    possible_titles = (ano - first_cup_year) // 4

    if number_titles > possible_titles:
        raise ImpossibleTitlesError()


# data = {
#     "name": "França",
#     "titles": -3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "2000-10-18"
# }

# print(data_processing(data))
# NegativeTitlesError: titles cannot be negative

# data = {
#     "name": "França",
#     "titles": 3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "1911-10-18"
# }

# print(data_processing(data))
# InvalidYearCupError: there was no world cup this year

# data = {
#     "name": "França",
#     "titles": 3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "1932-10-18"
# }

# print(data_processing(data))
# InvalidYearCupError: there was no world cup this year

# data = {
#     "name": "França",
#     "titles": 9,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "2002-10-18",
# }

# print(data_processing(data))
# ImpossibleTitlesError: impossible to have more titles than disputed cups

