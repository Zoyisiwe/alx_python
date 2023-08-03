"""This function checks if the object is exactly an instance of the speified class"""

def is_same_class(obj, a_class):
    """"The function uses isinsrance to see if the class is exactly like a given object"""
    return type(obj) is a_class
