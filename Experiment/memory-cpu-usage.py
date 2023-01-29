import time
import psutil
import numpy as np
import scipy.sparse as sparse
import matplotlib.pyplot as plt

# Start the timer
start_time = time.time()

# Initialize lists to store the memory and CPU usage
memory_usage = []
cpu_usage = []

# Run the solution
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

# Measure the memory and CPU usage every 0.5 seconds
while time.time() - start_time < 60:
    # Get the memory usage
    memory_info = psutil.virtual_memory()
    memory_usage.append(memory_info.used / (1024 ** 2))

    # Get the CPU usage
    cpu_usage.append(psutil.cpu_percent())

    # Wait for 0.5 seconds
    time.sleep(0.5)

# Plot the memory usage
plt.plot(memory_usage)
plt.xlabel("Time (seconds)")
plt.ylabel("Memory Usage (MB)")
plt.savefig('experimental-memory-usage.png')
plt.show()

# Plot the CPU usage
plt.plot(cpu_usage)
plt.xlabel("Time (seconds)")
plt.ylabel("CPU Usage (%)")
plt.savefig('experimental-cpu-usage.png')
plt.show()

