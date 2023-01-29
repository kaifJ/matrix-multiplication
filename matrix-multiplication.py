import numpy as np
import time

start = time.time()
# Generate random matrices A, B
matrixA = np.random.random((10**6, 10**6))
matrixB = np.random.random((10**3, 10**6))

# Multiply A and B to get matrixAB
matrixAB = np.matmul(matrixA, matrixB)
del matrixA
del matrixB

#Generate matrix C
matrixC = np.random.random((10**6, 1))

# Multiply matrixAB and C to get the final matrix D
D = np.matmul(matrixAB, matrixC)
end = time.time()


print(D)
print(f"time taken for the entire matrix multiplication is {end-start} seconds")