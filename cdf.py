import numpy as np
import matplotlib.pyplot as plt

# Generate random matrix matrixA
matrixA = np.random.random((10**6, 10**3))

# Flatten the matrixA to a 1-D array
flat_A = matrixA.flatten()

# Compute the histogram of the values in A
counts, bin_edges = np.histogram(flat_A, bins=100, density=True)

# Compute the cumulative distribution function
cdf = np.cumsum(counts)

# Plot the CDF
plt.plot(bin_edges[1:], cdf)
plt.xlabel("values")
plt.ylabel("cumulative probability")
plt.show()
