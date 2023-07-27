def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    finally:
        print("Inside result: {}".format(result))

    return result

# Test the function
#result = safe_print_division(10, 2)
#print("Returned value:", result)
