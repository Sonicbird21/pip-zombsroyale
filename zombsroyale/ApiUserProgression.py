from .ApiUserUpcomingReward import ApiUserUpcomingReward

class ApiUserProgression:
    def __init__(self, progression:dict) -> None:
        self.currentExperience:int = progression['currentExperience']
        self.requiredExperience:int = progression['requiredExperience']
        self.rewards:list[ApiUserUpcomingReward] = []
        for reward in progression['rewards']: self.rewards.append(ApiUserUpcomingReward(reward))
        self.isStale:bool = progression['isStale']

