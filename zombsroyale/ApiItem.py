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