from Telegram.connector import Connector

class HandlerMsn:

    def __init__(self):
        self.connector = Connector()
        self.list_msn = list()
        

    def refresh_msn(self):
        new_msns = self.connector.get_msn(5)
        a = 2


    def send_msn(self):
        pass

if __name__== "__main__":
    hm = HandlerMsn()
    hm.refresh_msn()