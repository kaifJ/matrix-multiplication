import threading
import time
import random
import statistics

def thread_function(num_array, n):
    sum = 0
    for i in range(n):
        sum += num_array[i]
    return

def main():
    max_n = 1000
    num_array = [random.randint(1, 10000) for i in range(max_n)]
    time_samples = []

    for j in range(1000):
        start_time = time.perf_counter()
        n = random.randint(1, max_n)
        thread = threading.Thread(target=thread_function, args=(num_array, n,))
        thread.start()
        thread.join()
        end_time = time.perf_counter()
        time_samples.append(end_time - start_time)

    print("Summary statistics:")
    print("Minimum time: ", min(time_samples))
    print("Maximum time: ", max(time_samples))
    print("Average time: ", statistics.mean(time_samples))
    print("Standard deviation: ", statistics.stdev(time_samples))

if __name__ == "__main__":
    main()
