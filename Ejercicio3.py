import matplotlib.pyplot as plt
from timeit import default_timer as timer

def if_else_loop(n):
    for i in range(n):
        if i % 2 == 0:
            pass  
        else:
            pass

# Define values of n manually (without NumPy)
n_values = [1, 10, 100, 1000, 10000, 100000]
times = []

# Measure execution times
for n in n_values:
    start = timer()
    for _ in range(5):  # Repeat measurement for better accuracy
        if_else_loop(n)
    end = timer()
    
    avg_time = (end - start) / 5  # Compute average time
    times.append(avg_time)
    print(f"Processing time for n={n} -> {avg_time:.8f} seconds")

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='b', label='Execution Time')

# Logarithmic scale on the X-axis
plt.xscale('log')

# Labels and title
plt.xlabel('Size of n (log scale)')
plt.ylabel('Execution time (s)')
plt.title('If-Then-Else Complexity O(n)')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Show the plot
plt.show()

