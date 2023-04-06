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