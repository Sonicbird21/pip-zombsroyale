import requests

class ApiLeaderboardTime:
    TIME_1_DAY = '24h'
    TIME_7_DAYS = '7d'
    TIME_1_MONTH = '1m'
    TIME_ALL_TIME = 'all'

class ApiLeaderboardMode:
    MODE_SOLO = 'solo'
    MODE_DUO = 'duo'
    MODE_SQUAD = 'squad'
    MODE_LIMITED_TIME_MODE = 'limited'

class ApiLeaderboardCategory:
    CATEGORY_KILLS = 'kills'
    CATEGORY_KILLS_PER_ROUND = 'kills_per_round'
    CATEGORY_WINS = 'wins'
    CATEGORY_PLAY_TIME = 'time_alive'
    CATEGORY_WINRATE = 'winrate'
    CATEGORY_TOP10 = 'top10'
    CATEGORY_GAMES_PLAYED = 'rounds'

class ApiLeaderboard():
    def __init__(self, time:ApiLeaderboardTime, mode:ApiLeaderboardMode, category:ApiLeaderboardCategory) -> None:
        self.time = time
        self.mode = mode
        self.category = category
    
    def ModifyTime(self, time:ApiLeaderboardTime) -> None:
        self.time = time
        
    def ModifyMode(self, mode:ApiLeaderboardMode) -> None:
        self.mode = mode

    def ModifyCategory(self, category:ApiLeaderboardCategory) -> None:
        self.category = category

    def Fetch(self) -> dict:
        res = requests.get("https://www.zombsroyale.io/api/leaderboard/live", params={"time":self.time,"mode":self.mode,"category":self.category}) 
        return res.json()