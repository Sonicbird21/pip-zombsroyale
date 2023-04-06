import requests
from .exceptions import *
from zombsroyale import ApiUserReward, ApiDate, ApiUserProgression, ApiClan, ApiUserLicense, ApiUserLicense, ApiUserPack, ApiUserSubscription, ApiUserIapTransaction, ApiRewardType, ApiResponseClanLeave, ApiResponseClanCreate, ApiResponseClanJoin

class ApiUser:
    def __init__(self, user:dict) -> None:
        self.rewards:list[ApiUserReward] = []
        for reward in user['rewards']: self.rewards.append(ApiUserReward(reward))
        self.id:int = user['user']['id']
        self.provider:str = user['user']['provider']
        self.identifier:str = user['user']['identifier']
        self.name:str = user['user']['name']
        self.avatar:str = user['user']['avatar']
        self.email:str = user['user']['email']
        self.friend_code:str = user['user']['friend_code']
        self.experience:int = user['user']['experience']
        self.level:int = user['user']['level']
        self.coins:int = user['user']['coins']
        self.gems:int = user['user']['gems']
        self.status:str = user['user']['status']
        self.created:ApiDate = ApiDate(user['user']['created'])
        self.updated:ApiDate = ApiDate(user['user']['updated'])
        self.key:str = user['user']['key']
        self.keyExpires:ApiDate = ApiDate(user['user']['keyExpires'])
        self.progression:ApiUserProgression = ApiUserProgression(user['user']['progression'])
        self.clans:list[ApiClan] = []
        for clan in user['user']['clans']: self.clans.append(ApiClan(clan))
        self.licenses:list[ApiUserLicense] = []
        for license in user['user']['licenses']: self.licenses.append(ApiUserLicense(license))
        self.packs:list[ApiUserPack] = []
        for pack in user['user']['packs']: self.packs.append(ApiUserPack(pack))
        self.subscriptions:list[ApiUserSubscription] = []
        for subscription in user['user']['subscriptions']: self.subscriptions.append(ApiUserSubscription(subscription))
        self.iaps:list[ApiUserIapTransaction] = []
        for iap in user['user']['iaps']: self.iaps.append(ApiUserIapTransaction(iap))

    @classmethod
    def KeyInit(cls, userKey:str):
        res = requests.get(f"https://www.zombsroyale.io/api/user/{userKey}")
        return cls(res.json())

    def Update(self) -> None:
        self.__init__(self.key)

    def GetUser(self) -> dict:
        """API Endpoint: https://www.zombsroyale.io/api/user/{userKey}"""
        res = requests.get(f"https://www.zombsroyale.io/api/user/{self.key}")
        return res.json()
    
    def BuyItem(self, itemId:int, quantity:int) -> dict:
        """API Endpoint: https://www.zombsroyale.io/api/user/{userKey}/buy?itemId={itemId}&quantity={quantity}"""
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/buy", params={"itemId": itemId, "quantity": quantity})
        return res.json()
    
    def BuyPack(self, packId:int, quantity:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/buy", params={"packId": packId, "quantity": quantity})
        return res.json()
    
    def BuyTimedDeal(self, timedDealId:int, quantity:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/buy", params={"timedDealId": timedDealId, "quantity": quantity})
        return res.json()
    
    def ClearUserSessions(self) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/clear-sessions")
        return res.json()
    
    def UpdateFriendCode(self, name:str) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/friend-code/update", params={"name": name})
        return res.json()
    
    def OpenPack(self, packId:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/pack/open", params={"packId": packId})
        return res.json()
    
    def GetRewards(self) -> dict:
        res = requests.get(f"https://www.zombsroyale.io/api/user/{self.key}/rewards")
        return res.json()
    
    def ClaimReward(self, type:ApiRewardType) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/user/{self.key}/rewards/claim", params={"type": type})
        return res.json()

    def JoinClan(self, clanId:int) -> ApiResponseClanJoin:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/{clanId}/join", params={"userKey": self.key})
        temp = res.json()
        return ApiResponseClanJoin(temp)

    def CreateClan(self, name:str, tag:str, description:str="") -> ApiResponseClanCreate:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/create", params={"userKey": self.key, "name": name, "tag": tag, "description": description})
        temp = res.json()
        return ApiResponseClanCreate(temp)
    
    def LeaveClan(self, clanId:int) -> ApiResponseClanLeave:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/{clanId}/leave", params={"userKey": self.key})
        temp = res.json()
        return ApiResponseClanLeave(temp)