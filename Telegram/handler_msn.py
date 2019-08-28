from Telegram.connector import Connector

class HandlerMsn:

    def __init__(self):
        self.connector = Connector()

    def refresh_msn(self):
        new_msns = self.connector.get_msn(5)
        a = 2

if __name__== "__main__":
    hm = HandlerMsn()
    hm.refresh_msn()