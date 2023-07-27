def raise_exception():
    raise TypeError("This is a type exception.")

# Test the function
try:
    raise_exception()
except TypeError as te:
    print("Expection raised")
