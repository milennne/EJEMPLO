#EJERCICIO 1 

from timeit import default_timer as timer
import matplotlib.pyplot as plt


def logarithms(n):
    i = 1
    while i <= n:
        i = i * 2 


n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []  

for n in n_values:
    start = timer()
    logarithms(n)
    end = timer()
    
    proc_time = end - start  # Calculamos el tiempo de ejecución
    times.append(proc_time)  # Almacenamos el tiempo correspondiente a ese n
    
    print(f"Tiempo de procesamiento para n = {n}: {proc_time} segundos")

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', linestyle='-', color='blue', label="Tiempo de procesamiento")
plt.title("Tiempo de Ejecución vs Tamaño de Entrada (O(log n))")
plt.xlabel("Tamaño de Entrada (n)")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.xscale('log')  # Escala logarítmica para visualizar mejor la gráfica
plt.yscale('log')  # También podemos usar escala logarítmica en el eje Y
plt.grid(True)
plt.legend()
plt.show()
