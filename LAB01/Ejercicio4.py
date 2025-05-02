from timeit import default_timer as timer
import matplotlib.pyplot as plt

def process_time(n):
    start = timer()

    for i in range(n):
        for j in range(n):
            pass  # Nested Loop Simulation

    end = timer()
    proc_time= end - start
    print(f"Time taken for n={n}: {proc_time} seconds")
    return proc_time
# Values ​​of n to test
n_values = [100, 400, 600, 800, 1000, 1100]
times = [process_time(n) for n in n_values]

# Graph the results
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', label='Processing time')
plt.xlabel("Input size (n)")
plt.ylabel("Time (seconds)")
plt.title("Processing time vs. Input size (O(n²))")
plt.legend()
plt.grid(True)
plt.show()
