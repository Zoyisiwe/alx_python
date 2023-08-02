"""This class  is based and worked upon the file 2-square"""

class Square:
    """This class has a private instance attribute
       with the value size that must be a integer and not less than 0 
       with the area of the square, and a property setter.
    """
    def __init__(self, size=0):
        self.size = size  # Call the property setter to validate the size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
