from Telegram.connector import Connector

class HandlerTelegram:

    def __init__(self):
        self.connector = Connector()
        self.list_conn = list()
        self.list_msn = list()
        

    def _filter_new_msn(self, list_msn):
        new_msns = list()
        for item_new in list_msn:
            new = True
            for item_list in self.list_msn:
                if str(item_list) is str(item_new):
                    new = False
            
            if new:
                new_msns.append(item_new)

        return new_msns
        

    def get_new_msn(self, channel):
        msns = self.connector.get_msn(channel, 0)
        new_msns = self._filter_new_msn(msns)
        
        return new_msns
       

    def _create_new_conexion(self):
        pass

        
if __name__== "__main__":
    ht = HandlerTelegram()
    new_msn = ht.get_new_msn("https://t.me/joinchat/AAAAAEovusdyxSfqrfCy2A")
    a = 2