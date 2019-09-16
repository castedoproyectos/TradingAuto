
from Process.target import Target
from Process.signal import Signal

class Trade():

    def __init__(self, pair = None,
                       type = None,
                       entry = None,
                       stoploss = None,
                       takeprofit = None):
        
        # Must
        self._pair = None
        self._type = None
        self._entry = None      # Class Target
        
        # No need (Class Target)
        self._stoploss = None
        self._takeprofit = None
        
        # Status
        self._running = None

        ## -- Msn of the trade
        self._list_msn = list()

        ## -- Analysis -- ##
        self._exit = None  
        self._duration = None
        self._earn = None

