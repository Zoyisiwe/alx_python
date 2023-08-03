"""This is a empty class"""


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


 