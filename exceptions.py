class NegativeTitlesError(Exception):
    def __init__(self):
        default_message = "titles cannot be negative"
        super().__init__(default_message)


class InvalidYearCupError(Exception):
    def __init__(self):
        default_message = "there was no world cup this year"
        super().__init__(default_message)


class ImpossibleTitlesError(Exception):
    def __init__(self):
        default_message = "impossible to have more titles than disputed cups"
        super().__init__(default_message)
