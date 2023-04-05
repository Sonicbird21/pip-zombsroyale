class ApiDate:
    def __init__(self, date:str, timezone_type:str, timezone:str) -> None:
        self.date = date
        self.timezone_type = timezone_type
        self.timezone = timezone