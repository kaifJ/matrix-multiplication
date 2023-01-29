import numpy as np
import scipy.sparse as sparse

# Dimensions of the matrices
m, k, n = 10**6, 10**3, 1

# Generate sparse matrices with random values between 0 and 1
A = sparse.random(m, k, density=0.1, format='csr', random_state=None, data_rvs=lambda size: np.random.rand(size))
B = sparse.random(k, m, density=0.1, format='csr', random_state=None, data_rvs=lambda size: np.random.rand(size))

# Multiply the matrices
AB = A.dot(B)

del A
del B

C = sparse.random(m, n, density=0.1, format='csr', random_state=None, data_rvs=lambda size: np.random.rand(size))
D = AB.dot(C)

print('done')
print(D)