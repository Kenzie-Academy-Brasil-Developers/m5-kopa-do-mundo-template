from utils import data_processing

if __name__ == "__main__":
    data = {
        "name": "França",
        "titles": 3,
        "top_scorer": "Zidane",
        "fifa_code": "FRA",
        "first_cup": "1934-10-18"
    }
    print(data_processing(data))
    ...