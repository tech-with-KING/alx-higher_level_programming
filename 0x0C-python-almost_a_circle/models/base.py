class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if self.id == None:
            self.id = __nb_objects = 0
        else:
            self.id = id
            
        
