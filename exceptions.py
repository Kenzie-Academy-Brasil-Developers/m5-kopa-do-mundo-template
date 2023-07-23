class NegativeTitlesError(Exception):
    def __init__(self, message="titles cannot be negative"):
        super().__init__(message)


class InvalidYearCupError(Exception):
    def __init__(self, message="there was no world cup this year"):
        super().__init__(message)


class ImpossibleTitlesError(Exception):
    def __init__(self, message="impossible to have more titles than disputed cups"):
        super().__init__(message)