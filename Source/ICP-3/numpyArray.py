import numpy as np

print('Matrix of size 20: ')
matrix1 = np.random.uniform(low=1, high=20, size=20)
print(matrix1)

# Reshape matrix to 4 X 5
print('4 X 5 reshaped matrix: ')
matrix2 = matrix1.reshape(4, 5)
print(matrix2)

# Find max in each row
print('Max values in each row: ')
maxR = (np.max(matrix2, axis=1).reshape(4, 1))
print(maxR)

# Replace the max value in each row with 0
print('Final matrix with max value replaced by 0: ')
matrix3 = (np.where(matrix2 == maxR, 0,  matrix2))
print(matrix3)
