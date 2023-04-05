class InvalidUserkeyError(Exception):
    def __init__(self, userkey):
        self.userkey = userkey

    def __str__(self):
        return f"Provided login token: {self.userkey} is not a valid userkey."