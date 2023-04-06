from zombsroyale import ApiDate, ApiUserReward

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
        #self.created:ApiDate = ApiDate(iap['created'])
        #self.updated:ApiDate = ApiDate(iap['updated'])

