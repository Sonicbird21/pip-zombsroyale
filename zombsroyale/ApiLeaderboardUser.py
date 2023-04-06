from .ApiLeaderboardPlayer import ApiLeaderboardPlayer

class ApiLeaderboardUser(ApiLeaderboardPlayer):
    def __init__(self, player: dict) -> None:
        super().__init__(player)
        self.rank:int = player['rank']