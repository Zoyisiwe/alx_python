"""This file is based on the previus file named 5-base_geometry"""

class BaseGeometry():
    """This is empty class"""
    def __dir__(cls):
        """control access to some inherited attributes"""
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr !='__init_subclass__':
                n_attributes.append(attr)
        return n_attributes 

    def area(self):
        """This is the area of the class"""
        raise Exception("area() is not implemented")  


    def integer_validator(self, name, value):
        """The function checks if the value is less or equal to 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")    


class Rectangle(BaseGeometry):
    """This class is a inheritance of BaseGeometry"""
    def __init__(self, width, height):
        """Inheritance appilied to a rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)