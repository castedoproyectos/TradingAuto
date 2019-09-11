from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from Common.utils import tprint

class Connector:

    def __init__(self):
        
        self._sesion_name = "test"
        self._hash_id = "526632"
        self._hash_num = "eeb7b94dc683848287857f8bfa03aa58"
        
        self._client = TelegramClient(self._sesion_name,
                                self._hash_id,
                                self._hash_num)
        self._client.start()


    def get_msn(self, channel, number_msn):
        channel_entity = self._client.get_entity(channel)

        posts = self._client(GetHistoryRequest(
            peer = channel_entity,
            limit = 1,
            offset_date = None,
            offset_id = 0,
            max_id = 0,
            min_id = 0,
            add_offset = number_msn,
            hash = 0))
    
    
        list_mensajes = list()
        for item in posts.messages[:]:
            new_msn = dict()
            new_msn = {'id': item.id, 
                       'id_parent': item.reply_to_msg_id,
                       'datetime': item.date,
                       'message': item.message}

            list_mensajes.append(new_msn)
            
        return list_mensajes