from zombsroyale import ApiUserReward
 
class ApiUserUpcomingReward(ApiUserReward):
    def __init__(self, reward:dict) -> None:
        super().__init__(reward)
        self.level:int = reward['level']