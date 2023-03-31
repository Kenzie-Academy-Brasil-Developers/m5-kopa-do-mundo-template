class NegativeTitlesError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidYearCupError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ImpossibleTitlesError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)