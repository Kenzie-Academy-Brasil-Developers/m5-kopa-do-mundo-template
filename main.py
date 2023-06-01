from utils import *
from exceptions import *

data = {
    "name": "França",
    "titles": -3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2000-10-18",
}
data2 = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "1911-10-18",
}
data3 = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}


if __name__ == "__main__":
    try:
        data_processing(data3)
    except NegativeTitlesError as err:
        print(err.message)
    except InvalidYearCupError as err:
        print(err.message)
    except ImpossibleTitlesError as err:
        print(err.message)