class ApiUserIapTransaction:
    def __init__(self, iap:dict) -> None:
        self.id:int = iap['id']
        self.user_id:int = iap['user_id']
        self.iap_id:int = iap['iap_id']
        self.cost_dollars:float = iap['cost_dollars']