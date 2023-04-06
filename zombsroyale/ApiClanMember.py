class ApiClanMember:
    def __init__(self, member:dict) -> None:
        self.type:str = member['type']
        self.friend_code:str = member['friend_code']
        self.name:str = member['name']
        self.avatar:str = member['avatar']
        self.status:str = member['status']