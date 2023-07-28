def no_c(my_string):
    filtered_chars = [char for char in my_string if char.lower() not in ('c', 'C')]
    
    new_string = ''.join(filtered_chars)
    return new_string

word = "School"
new_word = no_c(word)

print(no_c("School"))

#result = (no_c("Chicago"))
#print(result)

#result = (no_c("C is fun!"))
#print(result)
