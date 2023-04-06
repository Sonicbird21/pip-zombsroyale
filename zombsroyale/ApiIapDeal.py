from zombsroyale import ApiIap

class ApiIapDeal(ApiIap):
    def __init__(self, iap: dict) -> None:
        super().__init__(iap)