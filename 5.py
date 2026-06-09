# Function to add two matrices
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# Function to transpose a matrix
def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


# Function to multiply two matrices
def multiply_matrices(A, B):
    # Number of rows in A
    rows_A = len(A)
    # Number of columns in A
    cols_A = len(A[0])
    # Number of columns in B
    cols_B = len(B[0])
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Define two matrices
matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_B = [
    [7, 8, 9],[10, 11, 12]
]

# Add the matrices
added_matrix = add_matrices(matrix_A, matrix_B)
print("Added Matrix:")
for row in added_matrix:
    print(row)

# Transpose the first matrix
transposed_matrix_A = transpose_matrix(matrix_A)
print("\nTransposed Matrix A:")
for row in transposed_matrix_A:
    print(row)

# Define a second matrix for multiplication
matrix_B_for_multiplication = [
    [7, 10],
    [8, 11],
    [9, 12]
]

# Multiply the matrices
multiplied_matrix = multiply_matrices(matrix_A, matrix_B_for_multiplication)
print("\nMultiplied Matrix A and B:")
for row in multiplied_matrix:
    print(row)