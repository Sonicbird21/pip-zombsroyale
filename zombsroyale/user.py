import requests, zombsroyale as zr

class ApiRewardType:
    REWARD_FIRST = 'first'
    REWARD_GIFT = 'first'
    REWARD_RECURRING = 'recurring'
    REWARD_BONUS = 'bonus'
    REWARD_INSTAGRAM = 'instagram'
    REWARD_NITRO = 'nitro'
    REWARD_COMING_SOON = 'coming_soon'

class ApiUserIapTransaction:
    def __init__(self, iap:dict) -> None:
        self.id:int = iap['id']
        self.user_id:int = iap['user_id']
        self.iap_id:int = iap['iap_id']
        self.cost_dollars:float = iap['cost_dollars']

class ApiUserReward:
    def __init__(self, reward:dict) -> None:
        self.type:str = reward['type']
        self.itemId:int = reward['itemId']
        self.itemSku:str = reward['itemSku']
        self.packId:int = reward['packId']
        self.packSku:str = reward['packSku']
        self.quantity:int = reward['quantity']
        self.duplicateItemId:int = reward['duplicateItemId']

class ApiUserUpcomingReward(ApiUserReward):
    def __init__(self, reward:dict) -> None:
        super().__init__(reward)
        self.level:int = reward['level']

class ApiUserProgression:
    def __init__(self, progression:dict) -> None:
        self.currentExperience:int = progression['currentExperience']
        self.requiredExperience:int = progression['requiredExperience']
        self.rewards:list[ApiUserUpcomingReward] = []
        for reward in progression['rewards']: self.rewards.append(ApiUserUpcomingReward(reward))
        self.isStale:bool = progression['isStale']

class ApiUser:
    def __init__(self, userKey:str) -> None:
        res = requests.get(f"https://www.zombsroyale.io/api/user/{userKey}")
        temp = res.json()
        self.rewards:list[dict] = temp['rewards']
        self.id:int = temp['user']['id']
        self.provider:str = temp['user']['provider']
        self.identifier:str = temp['user']['identifier']
        self.name:str = temp['user']['name']
        self.avatar:str = temp['user']['avatar']
        self.email:str = temp['user']['email']
        self.friend_code:str = temp['user']['friend_code']
        self.experience:int = temp['user']['experience']
        self.level:int = temp['user']['level']
        self.coins:int = temp['user']['coins']
        self.gems:int = temp['user']['gems']
        self.status:str = temp['user']['status']
        self.created:zr.ApiDate = zr.ApiDate(temp['user']['created']['date'], temp['user']['created']['timezone_type'], temp['user']['created']['timezone'])
        self.updated:zr.ApiDate = zr.ApiDate(temp['user']['updated']['date'], temp['user']['updated']['timezone_type'], temp['user']['updated']['timezone'])
        self.key:str = temp['user']['key']
        self.keyExpires:zr.ApiDate = zr.ApiDate(temp['user']['keyExpires']['date'], temp['user']['keyExpires']['timezone_type'], temp['user']['keyExpires']['timezone'])
        self.progression:ApiUserProgression = ApiUserProgression(progression=temp['user']['progression'])
        self.clans:list[dict] = temp['user']['clans']
        self.licenses:list[dict] = temp['user']['licenses']
        self.packs:list[dict] = temp['user']['packs']
        self.subscriptions:list[dict] = temp['user']['subscriptions']
        self.iaps:list[ApiUserIapTransaction] = []
        for i in temp['user']['iaps']: self.iaps.append(ApiUserIapTransaction(i))

    def GetUser(self) -> dict:
        res = requests.get(f"https://www.zombsroyale.io/api/user/{self.key}")
        return res.json()
    
    def BuyItem(self, itemId:int, quantity:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/buy", params={"itemId":itemId,"quantity":quantity})
        return res.json()
    
    def BuyPack(self, packId:int, quantity:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/buy", params={"packId":packId,"quantity":quantity})
        return res.json()
    
    def BuyTimedDeal(self, timedDealId:int, quantity:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/buy", params={"timedDealId":timedDealId,"quantity":quantity})
        return res.json()
    
    def ClearUserSessions(self) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/clear-sessions")
        return res.json()
    
    def UpdateFriendCode(self, name:str) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/friend-code/update", params={"name":name})
        return res.json()
    
    def OpenPack(self, packId:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/pack/open", params={"packId":packId})
        return res.json()
    
    def GetRewards(self) -> dict:
        res = requests.get(f"https://www.zombsroyale.io/api/user/{self.key}/rewards")
        return res.json()
    
    def ClaimReward(self, type:ApiRewardType) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/rewards/claim", params={"type":type})
        return res.json()

    def JoinClan(self, clanId:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/{clanId}/join", params={"userKey":self.key})
        return res.json()

    def CreateClan(self, name:str, tag:str, description:str="") -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/create", params={"userKey":self.key,"name":name,"tag":tag,"description":description})
        return res.json()
    
    def LeaveClan(self, clanId:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/{clanId}/leave", params={"userKey":self.key})
        return res.json()
    
    