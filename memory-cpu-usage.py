import time
import psutil
import numpy as np
import matplotlib.pyplot as plt

# Start the timer
start_time = time.time()

# Initialize lists to store the memory and CPU usage
memory_usage = []
cpu_usage = []

# Run the solution
A = np.random.random((10**4, 10**3))
B = np.random.random((10**3, 10**4))

AB = np.matmul(A, B)
del A
del B

C = np.random.random((10**4, 1))
D = np.matmul(AB, C)

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
plt.savefig('memory-usage.png')
plt.show()

# Plot the CPU usage
plt.plot(cpu_usage)
plt.xlabel("Time (seconds)")
plt.ylabel("CPU Usage (%)")
plt.savefig('cpu-usage.png')
plt.show()

