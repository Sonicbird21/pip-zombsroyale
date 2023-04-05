import requests

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