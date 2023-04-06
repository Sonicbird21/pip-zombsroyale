import requests
from .exceptions import *
from .ApiUserReward import ApiUserReward
from .ApiDate import ApiDate
from .ApiUserProgression import ApiUserProgression
from .ApiClan import ApiClan
from .ApiUserLicense import ApiUserLicense
from .ApiUserPack import ApiUserPack
from .ApiUserSubscription import ApiUserSubscription
from .ApiUserIapTransaction import ApiUserIapTransaction
from .ApiRewardType import ApiRewardType

class ApiUser:
    def __init__(self, userKey:str) -> None:
        res = requests.get(f"https://www.zombsroyale.io/api/user/{userKey}")
        temp = res.json()
        self.rewards:list[ApiUserReward] = []
        for reward in temp['rewards']: self.rewards.append(ApiUserReward(reward))
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
        self.created:ApiDate = ApiDate(temp['user']['created'])
        self.updated:ApiDate = ApiDate(temp['user']['updated'])
        self.key:str = temp['user']['key']
        self.keyExpires:ApiDate = ApiDate(temp['user']['keyExpires'])
        self.progression:ApiUserProgression = ApiUserProgression(temp['user']['progression'])
        self.clans:list[ApiClan] = []
        for clan in temp['user']['clans']: self.clans.append(ApiClan(clan))
        self.licenses:list[ApiUserLicense] = []
        for license in temp['user']['licenses']: self.licenses.append(ApiUserLicense(license))
        self.packs:list[ApiUserPack] = []
        for pack in temp['user']['packs']: self.packs.append(ApiUserPack(pack))
        self.subscriptions:list[ApiUserSubscription] = []
        for subscription in temp['user']['subscriptions']: self.subscriptions.append(ApiUserSubscription(subscription))
        self.iaps:list[ApiUserIapTransaction] = []
        for iap in temp['user']['iaps']: self.iaps.append(ApiUserIapTransaction(iap))

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

    def JoinClan(self, clanId:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/{clanId}/join", params={"userKey": self.key})
        return res.json()

    def CreateClan(self, name:str, tag:str, description:str="") -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/create", params={"userKey": self.key, "name": name, "tag": tag, "description": description})
        return res.json()
    
    def LeaveClan(self, clanId:int) -> dict:
        res = requests.post(f"https://www.zombsroyale.io/api/clan/{clanId}/leave", params={"userKey": self.key})
        return res.json()