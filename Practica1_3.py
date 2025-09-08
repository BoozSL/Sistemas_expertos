import numpy as np
import matplotlib.pyplot as plt

# Datos reales: distancia recorrida (km) y gasto en gasolina (pesos)
distancias = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
gasto_real = np.array([20, 40, 58, 78, 100, 119, 140, 161, 180, 200])  
# Observa que no es exactamente proporcional, hay variaciones reales

# Rango de valores de w (costo por km) a evaluar
w_values = np.linspace(10, 25, 100)  # pesos por km
errors = []

# Función para calcular el MSE (Error cuadrático medio)
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Calcular el error para cada w
for w in w_values:
    gasto_predicho = w * distancias
    error = mean_squared_error(gasto_real, gasto_predicho)
    errors.append(error)

# Graficar w vs error
plt.figure(figsize=(8, 5))
plt.plot(w_values, errors, label='Error cuadrático medio')
plt.xlabel('Costo por km (w)')
plt.ylabel('Error')
plt.title('Búsqueda del costo promedio por km usando MSE')
plt.grid(True)
plt.legend()
plt.show()
