def safe_print_division(a, b):
    
    try:
        result = a / b

    except 0:
        print("Error: Division by zero.")

        return None
    
    finally:
        print("Inside result: {}" .format(result))

    return result
