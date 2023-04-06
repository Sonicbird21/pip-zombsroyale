class ApiUserReward:
    def __init__(self, reward:dict) -> None:
        self.type:str = reward['type']
        if reward.get('itemId'): self.itemId:int = reward['itemId']
        if reward.get('itemSku'): self.itemSku:str = reward['itemSku']
        if reward.get('packId'): self.packId:int = reward['packId']
        if reward.get('packSku'): self.packSku:str = reward['packSku']
        if reward.get('quantity'): self.quantity:int = reward['quantity']
        if reward.get('duplicateItemId'): self.duplicateItemId:int = reward['duplicateItemId']