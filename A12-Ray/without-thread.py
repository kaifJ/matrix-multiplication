import random
import time
import statistics

def thread_function(num_array, N):
    total = sum(num_array[:N])
    return total

def main():
    max_N = 1000
    num_array = [random.randint(1, 10000) for _ in range(max_N)]
    time_samples = []
    
    for j in range(1000):
        start_time = time.monotonic()
        N = random.randint(1, max_N)
        thread_function(num_array, N)
        end_time = time.monotonic()
        time_samples.append(end_time - start_time)
    
    print("Summary statistics:")
    print("Minimum time: ", min(time_samples))
    print("Maximum time: ", max(time_samples))
    print("Average time: ", statistics.mean(time_samples))
    print("Standard deviation: ", statistics.stdev(time_samples))

if __name__ == "__main__":
    main()