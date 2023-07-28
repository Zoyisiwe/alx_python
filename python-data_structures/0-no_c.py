def no_c(my_string):
    # Create a list with all characters except 'c' and 'C'
    filtered_chars = [char for char in my_string if char.lower() not in ('c', 'C')]
    
    # Join the list elements to form the new string
    new_string = ''.join(filtered_chars)
    return new_string

# Test the function
result = no_c("Holberton School")
result = no_c("Chicago")
result = no_c("C is fun!")
print(result)
