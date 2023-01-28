import numpy as np

# Generate random matrices A, B, and C with the specified dimensions
matrixA = np.random.random((106, 103))
matrixB = np.random.random((103, 106))
matrixC = np.random.random((106, 1))

# Multiply A and B to get matrixAB
matrixAB = np.matmul(matrixA, matrixB)

# Multiply matrixAB and C to get the final matrix D
D = np.matmul(matrixAB, matrixC)

print(D)
