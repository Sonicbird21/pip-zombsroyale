class ApiPackReward:
    def __init__(self, reward:dict) -> None:
        self.id:int = reward['id']
        self.pack_id:int = reward['pack_id']
        self.item_id:int = reward['item_id']
        self.weighting:float = reward['weighting']