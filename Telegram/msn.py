import datetime
class Msn:

    def __init__(self, id, id_parent, timedate, text):
        self.id = id
        self.id_parent = id_parent
        self.timedate = timedate
        self.text = text
    
    # OverWritte
    def __str__(self):
        string = None
        if self.id_parent is None:
            string = str(self.id) + str(self.timedate) + self.text
        
        else:
            string = str(self.id) + str(self.id_parent) + str(self.timedate) + self.text
        
        return string 
