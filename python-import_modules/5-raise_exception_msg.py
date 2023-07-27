def raise_exception_msg(message=""):
    raise NameError(message)

'''try:
    raise_exception_msg("C is fun")
except NameError as e:
    print(f"Error: {e}")'''

try:
    message = "C is fun"
    raise_exception_msg(message)
except NameError as ne:
    print(ne)
