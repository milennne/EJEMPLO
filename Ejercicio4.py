import timeit
import matplotlib.pyplot as plt

def process_time(n):
    start = timeit.default_timer()

    for i in range(n):
        for j in range(n):
            pass  # Simulación del bucle anidado

    end = timeit.default_timer()
    return end - start

# Valores de n a probar
n_values = [100, 400, 600, 800, 1000, 1100]
times = [process_time(n) for n in n_values]

# Graficar los resultados
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', label='Tiempo de procesamiento')
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de procesamiento vs. Tamaño de entrada (O(n²))")
plt.legend()
plt.grid(True)
plt.show()