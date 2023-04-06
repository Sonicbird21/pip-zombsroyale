from zombsroyale import ApiUser

class ApiResponseClanLeave:
    def __init__(self, response:dict) -> None:
        self.user:ApiUser = ApiUser(response['user'])