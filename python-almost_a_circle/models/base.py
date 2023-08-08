"""The begining of the network project in ALX"""

class Base:
    """This class is the base of other classes in this directory"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """This ia a class construtor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
