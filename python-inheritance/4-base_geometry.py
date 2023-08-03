"""This class is based on the file 3-base_geometry"""


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