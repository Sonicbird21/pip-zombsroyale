class ApiDate:
    def __init__(self, date:str) -> None:
        self.date = date['date']
        self.timezone_type = date['timezone_type']
        self.timezone = date['timezone']