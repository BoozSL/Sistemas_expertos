from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Datos de ejemplo: [duración(min), edad recomendada, género]
# Género: 0 = Acción, 1 = Comedia, 2 = Animación
X = [
    [120, 16, 0],  # Película de acción, adolescente
    [90, 12, 1],   # Comedia ligera
    [100, 7, 2],   # Animación para niños
    [150, 18, 0],  # Acción para adultos
    [95, 12, 1],   # Comedia
    [85, 7, 2],    # Animación corta
    [130, 16, 0],  # Acción
    [105, 7, 2]    # Animación más larga
]

# Etiquetas (gustó: 1, no gustó: 0)
y = [1, 1, 1, 0, 1, 1, 0, 1]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo Random Forest
modelo = RandomForestClassifier(n_estimators=5, random_state=42)
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

print(" Precisión del modelo:", accuracy_score(y_test, y_pred))

# Probar con un ejemplo nuevo
nueva_pelicula = [[110, 12, 1]]  # Comedia de 110 min, recomendada para 12+
prediccion = modelo.predict(nueva_pelicula)

if prediccion[0] == 1:
    print(" Recomendación: ¡A esta persona le gustará la película!")
else:
    print("Recomendación: Probablemente no le guste.")



