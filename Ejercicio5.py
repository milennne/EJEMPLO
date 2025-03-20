import matplotlib.pyplot as plt
from timeit import default_timer as timer

def consecutive_loops(n):
    for i in range(n):
        pass  
    for i in range(n):
        for j in range(n):
            pass  

n_values = [100, 400, 600, 800, 1000, 1100]
times = []

for n in n_values:
    start = timer()
    for _ in range(5):  
        consecutive_loops(n)
    end = timer()
    
    avg_time = (end - start) / 5  
    times.append(avg_time)
    print(f"Processing time for n={n} -> {avg_time:.8f} seconds")

plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='r', label=r"$O(n^2)$")

plt.xlabel("Tamaño de n")
plt.ylabel("Tiempo de Ejecución (s)")
plt.title("Tiempo de Ejecución vs. n (O(n²))")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)

plt.show()
