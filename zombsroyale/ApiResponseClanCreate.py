from zombsroyale import ApiUser, ApiClan

class ApiResponseClanCreate:
    def __init__(self, response:dict) -> None:
        self.user:ApiUser = ApiUser(response['user'])
        self.clan:ApiClan = ApiClan(response['clan'])