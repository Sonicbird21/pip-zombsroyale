class ApiUserSubscription:
    def __init__(self, subscription:dict) -> None:
        self.id:int = subscription['id']
        self.user_id:int = subscription['user_id']
        self.iap_id:int = subscription['iap_id']