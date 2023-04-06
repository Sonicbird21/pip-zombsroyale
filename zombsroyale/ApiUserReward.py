class ApiUserReward:
    def __init__(self, reward:dict) -> None:
        self.type:str = reward['type']
        self.itemId:int = reward['itemId']
        self.itemSku:str = reward['itemSku']
        self.packId:int = reward['packId']
        self.packSku:str = reward['packSku']
        self.quantity:int = reward['quantity']
        self.duplicateItemId:int = reward['duplicateItemId']