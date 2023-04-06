class ApiUserPack:
    def __init__(self, pack:dict) -> None:
        self.id:int = pack['id']
        self.user_id:int = pack['user_id']
        self.item_id:int = pack['item_id']
        self.quantity:int = pack['quantity']