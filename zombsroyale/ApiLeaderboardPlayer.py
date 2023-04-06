import datetime

class ApiLeaderboardPlayer:
    def __init__(self, player:dict) -> None:
        self.name:str = player['name']
        self.rounds:int = player['rounds']
        self.wins:int = player['wins']
        self.top10:int = player['top10']
        self.winrate:float = player['winrate']
        self.kills:int = player['kills']
        self.kills_per_round:float = player['kills_per_round']
        self.time_alive:int = player['time_alive']
    
    def ConvertTime(self) -> str:
        return datetime.timedelta(seconds=self.time_alive)