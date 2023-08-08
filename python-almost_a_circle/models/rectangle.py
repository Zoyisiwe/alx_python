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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """Function for setter and getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Function for setter and getter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """Function for setter and getter"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Function for setter and getter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """Function for setter and getter"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Function for setter and getter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This is a public method that adds the function area"""
        return self.__width * self.__height
    
    def display(self):
        """A public method of display and prints in stdout"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)


    def __str__(self):
        """This method overrides the other classes when called"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)