from .ApiDate import ApiDate

class ApiUserPack:
    def __init__(self, pack:dict) -> None:
        self.id:int = pack['id']
        self.obtained:ApiDate = ApiDate(pack['obtained'])
        self.updated:ApiDate = ApiDate(pack['updated'])
        self.user_id:int = pack['user_id']
        self.pack_id:int = pack['pack_id']
        self.quantity:int = pack['quantity']