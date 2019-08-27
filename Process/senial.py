
from target import Target

class Senial():

    def __init__(self, pair = None,
                       type = None,
                       entry = None,
                       stoploss = None,
                       takeprofit = None):
        
        self.pair = pair
        self.type = type
        self.entry = entry
        self.stoploss = stoploss
        self.takeprofit = takeprofit
        
        #############################

        self.running = None

        # TODO Hacer las cuentas
        self.duration = None
        self.earn = None

