class ApiChatMessage:
    def __init__(self, message:dict) -> None:
        self.type:str = message['type']
        self.clan_id:str = message['clan_id']
        self.user_id:str = message['user_id']
        self.friend_code:str = message['friend_code']
        self.sent:str = message['sent']
        self.body:str = message['body']