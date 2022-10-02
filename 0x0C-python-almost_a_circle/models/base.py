# #!/usr/bin/python3
'''Base this class initializes many
 instance of the same object it is the begining of what i want to do'''


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        '''function: __init__() Returns
        the initialized items
        '''
        self.id = Base.__nb_objects
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
