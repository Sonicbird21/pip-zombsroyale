import requests
from .ApiLeaderboardTime import ApiLeaderboardTime
from .ApiLeaderboardMode import ApiLeaderboardMode
from .ApiLeaderboardCategory import ApiLeaderboardCategory
from .ApiLeaderboardPlayer import ApiLeaderboardPlayer
from .ApiLeaderboardUser import ApiLeaderboardUser

class ApiLeaderboard:
    def __init__(self, time:ApiLeaderboardTime, mode:ApiLeaderboardMode, category:ApiLeaderboardCategory) -> None:
        self.time:ApiLeaderboardTime = time
        self.mode:ApiLeaderboardMode = mode
        self.category:ApiLeaderboardCategory = category
        res = requests.get("https://www.zombsroyale.io/api/leaderboard/live", params={"time": self.time, "mode": self.mode, "category": self.category}) 
        temp = res.json()
        self.players:list[ApiLeaderboardPlayer] = []
        for player in temp['players']: self.players.append(ApiLeaderboardPlayer(player))
        self.user:ApiLeaderboardUser|None = ApiLeaderboardUser(temp['user']) if temp['user'] is not None else None

    def ModifyTime(self, time:ApiLeaderboardTime) -> None:
        self.time = time

    def ModifyMode(self, mode:ApiLeaderboardMode) -> None:
        self.mode = mode

    def ModifyCategory(self, category:ApiLeaderboardCategory) -> None:
        self.category = category
    
    def Update(self):
        res = requests.get("https://www.zombsroyale.io/api/leaderboard/live", params={"time": self.time, "mode": self.mode, "category": self.category}) 
        temp = res.json()
        self.players = []
        for player in temp['players']: self.players.append(ApiLeaderboardPlayer(player))
        self.user = ApiLeaderboardUser(temp['user']) if temp['user'] is not None else None