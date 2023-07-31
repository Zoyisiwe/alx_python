def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char

sentence= ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))


# Test the function
'''result1 = multiple_returns("Hello, World!")
result2 = multiple_returns("Python")
result3 = multiple_returns("")

print(result1)  # Output: (13, 'H')
print(result2)  # Output: (6, 'P')
print(result3)  # Output: (0, None)'''
