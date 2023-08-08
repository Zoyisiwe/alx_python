"""This is a inheritance from the base file(class)"""

# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    """The class that inherited from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Function for setter and getter"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Function for setter and getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Function for setter and getter"""
        self.__width = value
    
    @property
    def height(self):
        """Function for setter and getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Function for setter and getter"""
        self.__height = value
    
    @property
    def x(self):
        """Function for setter and getter"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Function for setter and getter"""
        self.__x = value
    
    @property
    def y(self):
        """Function for setter and getter"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Function for setter and getter"""
        self.__y = value
