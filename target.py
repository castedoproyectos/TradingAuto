class Target():
    """ 
    Esta clase permite definir un tarjet. Lo que 
    equivaldria a un stoploss, o un takeproffit. Definiendo
    el valor de este, si ha sido alcanzado y la fecha y hora a 
    la que se alcanza.
    """
    def __init__(self, value = None, reach = None, datetime = None):

        self.value = value
        self.reach = reach
        self.datetime = datetime

    def is_reach(self):
        if self.datetime is None:
            return False
        else:
            return True
    
    
