import requests
from .ApiShopSection import ApiShopSection
from .ApiItem import ApiItem
from .ApiPack import ApiPack
from .ApiTimedDeal import ApiTimedDeal
from .ApiIap import ApiIap

class ApiShop:
    def __init__(self) -> None:
        res = requests.get("https://www.zombsroyale.io/api/shop/available")
        temp = res.json()
        self.items:list[ApiItem] = []
        for item in temp['items']: self.items.append(ApiItem(item))
        self.packs:list[ApiPack] = []
        for pack in temp['packs']: self.packs.append(ApiPack(pack))
        self.timedDeals:list[ApiTimedDeal] = []
        for timedDeal in temp['timedDeals']: self.timedDeals.append(ApiTimedDeal(timedDeal))
        self.iaps:list[ApiIap] = []
        for iap in temp['iaps']: self.iaps.append(ApiIap(iap))
        
    def Update(self):
        res = requests.get("https://www.zombsroyale.io/api/shop/available")
        temp = res.json()
        self.items:list[ApiItem] = []
        for item in temp['items']: self.items.append(ApiItem(item))
        self.packs:list[ApiPack] = []
        for pack in temp['packs']: self.packs.append(ApiPack(pack))
        self.timedDeals:list[ApiTimedDeal] = []
        for timedDeal in temp['timedDeals']: self.timedDeals.append(ApiTimedDeal(timedDeal))
        self.iaps:list[ApiIap] = []
        for iap in temp['iaps']: self.iaps.append(ApiIap(iap))
    
