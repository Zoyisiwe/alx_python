def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range (0, len(row)):
            if i == len(row) - 1 :
                print("{:d}" .format(row[i]))
            else:
                print("{:d}" .format(row[i]), end=" ") 

print()

# Test the function
'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)'''
