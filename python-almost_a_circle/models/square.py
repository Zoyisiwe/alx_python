"""This is a inheritance from the rectangle file(class)"""

# models/square.py

from models.rectangle import Rectangle

class Square(Rectangle):
    """This class is inherited from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """This function is a class constructor"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Calling the super class"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Calling the super class"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Counts the number of arguments and returns the answer"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == "size":
                    self.width = value
                    self.height = value
    
    def __str__(self):
        """Overloading this method from the rectangle file"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
