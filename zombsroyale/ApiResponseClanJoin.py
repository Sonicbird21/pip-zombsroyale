from zombsroyale import ApiUser, ApiClan

class ApiResponseClanJoin:
    def __init__(self, response:dict) -> None:
        self.user = ApiUser(response['user'])
        self.clan = ApiClan(response['clan'])