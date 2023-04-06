from zombsroyale import ApiPackReward

class ApiPack:
    def __init__(self, pack:dict) -> None:
        self.id:int = pack['id']
        self.sku:str = pack['sku']
        self.name:str = pack['name']
        self.cost_coins:int = pack['cost_coins']
        self.cost_gems:int = pack['cost_gems']
        self.rewards:list[ApiPackReward] = []
        for reward in pack['rewards']: self.rewards.append(ApiPackReward(reward))