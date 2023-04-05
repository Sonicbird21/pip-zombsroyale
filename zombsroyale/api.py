import requests
from .exceptions import *

class ApiChatMessage:
    def __init__(self, message:dict) -> None:
        self.type:str = message['type']
        self.clan_id:str = message['clan_id']
        self.user_id:str = message['user_id']
        self.friend_code:str = message['friend_code']
        self.sent:str = message['sent']
        self.body:str = message['body']

class ApiClanMember:
    def __init__(self, member:dict) -> None:
        self.type:str = member['type']
        self.friend_code:str = member['friend_code']
        self.name:str = member['name']
        self.avatar:str = member['avatar']
        self.status:str = member['status']

class ApiClan:
    def __init__(self, clan:dict) -> None:
        self.id:str = clan['id']
        self.creator_id:str = clan['creator_id']
        self.tag:str = clan['tag']
        self.name:str = clan['name']
        self.description:str = clan['description']
        self.privacy:str = clan['privacy']
        self.region:str = clan['region']
        self.total_members:str = clan['total_members']
        self.max_members:str = clan['max_members']
        self.members:list[ApiClanMember] = []
        for member in clan['members']: self.members.append(ApiClanMember(member))
        self.messages:list[ApiChatMessage] = []
        for message in clan['messages']: self.messages.append(ApiChatMessage(message))

class ApiShopSection:
    SECTION_ITEMS = 'items'
    SECTION_PACKS = 'packs'
    SECTION_IN_APP_PURCHASES = 'iaps'
    SECTION_TIMED_DEALS = 'timedDeals'
    SESECTION_ALL = 'all'

class ApiShop:
    def __init__(self, sections:list[ApiShopSection]) -> None:
        self.sections:list[ApiShopSection] = sections

    def ModifySections(self, sections:list[ApiShopSection]) -> None:
        self.sections = sections

    def Fetch(self) -> dict:
        res = requests.get("https://www.zombsroyale.io/api/shop/available", params={"sections": self.sections})
        return res.json()
    
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

class ApiUserIapTransaction:
    def __init__(self, iap:dict) -> None:
        self.id:int = iap['id']
        self.user_id:int = iap['user_id']
        self.iap_id:int = iap['iap_id']
        self.cost_dollars:float = iap['cost_dollars']

class ApiPackReward:
    def __init__(self, reward:dict) -> None:
        self.id:int = reward['id']
        self.pack_id:int = reward['pack_id']
        self.item_id:int = reward['item_id']
        self.item_sku:str = reward['item_sku']
        self.weighting:float = reward['weighting']

class ApiItem:
    def __init__(self, item:dict) -> None:
        self.id:int = item['id']
        self.sku:str = item['sku']
        self.name:str = item['name']
        self.type:str = item['type']
        self.category:str = item['category']
        self.rarity:str = item['rarity']
        self.cost_coins:int = item['cost_coins']
        self.cost_gems:int = item['cost_gems']
        self.is_stock:bool = item['is_stock']
        self.can_purchase:bool = item['can_purchase']
        self.order:int = item['order']

class ApiPack:
    def __init__(self, pack:dict) -> None:
        self.id:int = pack['id']
        self.sku:str = pack['sku']
        self.name:str = pack['name']
        self.cost_coins:int = pack['cost_coins']
        self.cost_gems:int = pack['cost_gems']
        self.rewards:list[ApiPackReward] = []
        for reward in pack['rewards']: self.rewards.append(ApiPackReward(reward))

class ApiIap:
    def __init__(self, iap:dict) -> None:
        self.id:int = iap['id']
        self.sku:str = iap['sku']
        self.name:str = iap['name']
        self.type:str = iap['type']
        self.xsolla_id:int = iap['xsolla_id']
        self.apple_id:str = iap['apple_id']
        self.google_id:str = iap['google_id']
        self.discord_id:str = iap['discord_id']
        self.cost_dollars:float = iap['cost_dollars']
        self.can_purchase:bool = iap['can_purchase']
        self.rewards:list[ApiUserReward] = []
        for reward in iap['rewards']: self.rewards.append(ApiUserReward(reward))
        self.created:ApiDate = ApiDate(iap['created']['date'], iap['created']['timezone_type'], iap['created']['timezone'])
        self.updated:ApiDate = ApiDate(iap['updated']['date'], iap['updated']['timezone_type'], iap['updated']['timezone'])

class ApiIapDeal(ApiIap):
    def __init__(self, iap: dict) -> None:
        super().__init__(iap)

class ApiTimedDeal:
    def __init__(self, item:dict) -> None:
        self.id:int = item['id']
        self.sku:str = item['sku']
        self.name:str = item['name']
        self.cost_coins:int = item['cost_coins']
        self.cost_gems:int = item['cost_gems']
        self.undiscounted_cost_coins:int = item['undiscounted_cost_coins']
        self.undiscounted_cost_gems:int = item['undiscounted_cost_gems']
        self.can_purchase:bool = item['can_purchase']
        self.order:int = item['order']

class ApiUserLicense:
    def __init__(self, license:dict) -> None:
        self.id:int = license['id']
        self.user_id:int = license['user_id']
        self.item_id:int = license['item_id']
        self.quantity:int = license['quantity']

class ApiUserPack:
    def __init__(self, pack:dict) -> None:
        self.id:int = pack['id']
        self.user_id:int = pack['user_id']
        self.item_id:int = pack['item_id']
        self.quantity:int = pack['quantity']

class ApiUserSubscription:
    def __init__(self, subscription:dict) -> None:
        self.id:int = subscription['id']
        self.user_id:int = subscription['user_id']
        self.iap_id:int = subscription['iap_id']

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
        res = requests.get("https://www.zombsroyale.io/api/leaderboard/live", params={"time": self.time, "mode": self.mode, "category": self.category}) 
        return res.json()
    
class ApiRewardType:
    REWARD_FIRST = 'first'
    REWARD_GIFT = 'first'
    REWARD_RECURRING = 'recurring'
    REWARD_BONUS = 'bonus'
    REWARD_INSTAGRAM = 'instagram'
    REWARD_NITRO = 'nitro'
    REWARD_COMING_SOON = 'coming_soon'

class ApiDate:
    def __init__(self, date:str, timezone_type:str, timezone:str) -> None:
        self.date = date
        self.timezone_type = timezone_type
        self.timezone = timezone

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
        self.created:ApiDate = ApiDate(temp['user']['created']['date'], temp['user']['created']['timezone_type'], temp['user']['created']['timezone'])
        self.updated:ApiDate = ApiDate(temp['user']['updated']['date'], temp['user']['updated']['timezone_type'], temp['user']['updated']['timezone'])
        self.key:str = temp['user']['key']
        self.keyExpires:ApiDate = ApiDate(temp['user']['keyExpires']['date'], temp['user']['keyExpires']['timezone_type'], temp['user']['keyExpires']['timezone'])
        self.progression:ApiUserProgression = ApiUserProgression(progression=temp['user']['progression'])
        self.clans:list[dict] = temp['user']['clans']
        self.licenses:list[ApiUserLicense] = []
        for license in temp['user']['licenses']: self.licenses.append(ApiUserLicense(license))
        self.packs:list[ApiUserPack] = []
        for pack in temp['user']['packs']: self.packs.append(ApiUserPack(pack))
        self.subscriptions:list[ApiUserSubscription] = []
        for subscription in temp['user']['subscriptions']: self.subscriptions.append(ApiUserSubscription(subscription))
        self.iaps:list[ApiUserIapTransaction] = []
        for iap in temp['user']['iaps']: self.iaps.append(ApiUserIapTransaction(iap))

    def GetUser(self) -> dict:
        res = requests.get(f"https://www.zombsroyale.io/api/user/{self.key}")
        return res.json()
    
    def BuyItem(self, itemId:int, quantity:int) -> dict:
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