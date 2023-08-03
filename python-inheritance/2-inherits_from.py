"""This function checks if a object is inherited directly/indirectly"""

def inherits_from(obj, a_class):
    """The function checks if the object is inherited directly or indirectly"""
    
    return isinstance(obj, a_class) and type(obj) != a_class
