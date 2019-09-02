from Telegram.connector import Connector

class HandlerMsn:

    def __init__(self):
        self.connector = Connector()
        self.list_msn = list()
        
    def filter_new_msn(self, list_msn):
        """ Recorre todos los elemententos de la lista introducida 
        correspondientes con mensajes para realizar un filtrado de estos y
        devolver aquellos que son nuevos.
        
        Arguments:
            list_msn {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        new_msns = list()
        for item_new in list_msn:
            new = True
            for item_list in self.list_msn:
                if str(item_list) is str(item_new):
                    new = False
            
            if new:
                new_msns.append(item_new)

        return new_msns
        

    def refresh_msn(self):
        new_msns = self.connector.get_msn(5)
        real_new_msns = self.filter_new_msn(new_msns)
        
        a = 2


if __name__== "__main__":
    hm = HandlerMsn()
    hm.refresh_msn()