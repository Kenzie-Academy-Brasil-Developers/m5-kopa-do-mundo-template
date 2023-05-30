from utils import *


def main():
    data = {
        "name": "França",
        "titles": -3,
        "top_scorer": "Zidane",
        "fifa_code": "FRA",
        "first_cup": "2000-10-18"
    }

    # print(data_processing(data))

    data = {
        "name": "França",
        "titles": 3,
        "top_scorer": "Zidane",
        "fifa_code": "FRA",
        "first_cup": "1911-10-18"
    }

    # print(data_processing(data))

    data = {
        "name": "França",
        "titles": 3,
        "top_scorer": "Zidane",
        "fifa_code": "FRA",
        "first_cup": "1932-10-18"
    }

    # print(data_processing(data))

    data = {
        "name": "França",
        "titles": 9,
        "top_scorer": "Zidane",
        "fifa_code": "FRA",
        "first_cup": "2002-10-18",
    }

    print(data_processing(data))


if __name__ == "__main__":
    main()
