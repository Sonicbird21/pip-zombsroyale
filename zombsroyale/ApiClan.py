from .ApiChatMessage import ApiChatMessage
from .ApiClanMember import ApiClanMember

class ApiClan:
    def __init__(self, clan:dict) -> None:
        self.id:str = clan['id']
        self.creator_id:str = clan['creator_id']
        self.tag:str = clan['tag']
        self.name:str = clan['name']
        self.description:str = clan['description']
        self.privacy:str = clan['privacy']
        self.region:str = clan['region']
        self.total_members:str = clan['total_members']
        self.max_members:str = clan['max_members']
        self.members:list[ApiClanMember] = []
        for member in clan['members']: self.members.append(ApiClanMember(member))
        self.messages:list[ApiChatMessage] = []
        for message in clan['messages']: self.messages.append(ApiChatMessage(message))