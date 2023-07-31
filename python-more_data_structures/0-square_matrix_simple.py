def square_matrix_simple(matrix=[]):
    # Create an empty matrix of the same size as the input matrix
    squared_matrix = [[0 for _ in range(len(matrix[0]))] 
                      for _ in range(len(matrix))]

    # Calculate the square value of each element and store it in the new matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_matrix[i][j] = matrix[i][j] ** 2

    return squared_matrix

# Test the function
'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(matrix)
print(result)'''
