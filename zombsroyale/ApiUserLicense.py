class ApiUserLicense:
    def __init__(self, license:dict) -> None:
        self.id:int = license['id']
        self.user_id:int = license['user_id']
        self.item_id:int = license['item_id']
        self.quantity:int = license['quantity']