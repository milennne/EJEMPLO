#EJERCICIO 2


import matplotlib.pyplot as plt
from timeit import default_timer as timer

n_values = [10**2, 10**3, 10**4, 10**5, 10**6]

processing_times = []

for n in n_values:
    start = timer()  

    for i in range(0, n):  # Simple loop
        pass  # The print is removed to make the measurement more accurate

    end = timer()  

    proc_time = end - start  
    processing_times.append(proc_time)  

    print(f"Processing time for n = {n} -> {proc_time} seconds")

plt.figure(figsize=(10, 6))
plt.plot(n_values, processing_times, marker='o', linestyle='-', color='blue', label='Processing time')
plt.title('Processing Time vs. Input Size (n)')
plt.xlabel('Input Size (n)')
plt.ylabel('Processing Time (seconds)')
plt.xscale('log') 
plt.yscale('log')  
plt.grid(True)
plt.legend()
plt.show()

