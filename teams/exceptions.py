class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = {"error": f"{message}"}


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = {"error": f"{message}"}


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = {"error": f"{message}"}
