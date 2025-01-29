import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada (X) y las etiquetas de salida (y)
X = np.array([[0, 0],  # Entrada 1
              [0, 1],  # Entrada 2
              [1, 0],  # Entrada 3
              [1, 1]]) # Entrada 4

y = np.array([[0],  # Salida esperada para entrada 1
              [1],  # Salida esperada para entrada 2
              [1],  # Salida esperada para entrada 3
              [0]]) # Salida esperada para entrada 4

# Inicialización de pesos y bias
np.random.seed(1)  # Semilla para reproducibilidad
input_neurons = 2  # Número de neuronas en la capa de entrada
hidden_neurons = 3 # Número de neuronas en la capa oculta
output_neurons = 1 # Número de neuronas en la capa de salida

# Pesos entre capa de entrada y capa oculta
weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
# Pesos entre capa oculta y capa de salida
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))

# Bias de la capa oculta
bias_hidden = np.random.uniform(size=(1, hidden_neurons))
# Bias de la capa de salida
bias_output = np.random.uniform(size=(1, output_neurons))

# Hiperparámetros
epochs = 10000        # Número de épocas (iteraciones)
learning_rate = 0.1   # Tasa de aprendizaje

# Entrenamiento de la red neuronal
for epoch in range(epochs):
    # Propagación hacia adelante (feedforward)
    # Cálculo de la entrada y salida de la capa oculta
    input_hidden = np.dot(X, weights_input_hidden) + bias_hidden
    output_hidden = sigmoid(input_hidden)

    # Cálculo de la entrada y salida de la capa de salida
    input_output = np.dot(output_hidden, weights_hidden_output) + bias_output
    output = sigmoid(input_output)

    # Retropropagación
    # Cálculo del error (diferencia entre la salida esperada y la salida obtenida)
    error = y - output
    
    # Calcular los deltas y ajustar los pesos
    delta_output = error * sigmoid_derivative(output)  # Delta para la capa de salida
    error_hidden = delta_output.dot(weights_hidden_output.T)  # Error de la capa oculta
    delta_hidden = error_hidden * sigmoid_derivative(output_hidden)  # Delta para la capa oculta

    # Actualizar pesos y bias
    # Actualización de pesos y bias entre la capa oculta y la capa de salida
    weights_hidden_output += output_hidden.T.dot(delta_output) * learning_rate
    bias_output += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
    # Actualización de pesos y bias entre la capa de entrada y la capa oculta
    weights_input_hidden += X.T.dot(delta_hidden) * learning_rate
    bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

# Resultados finales después del entrenamiento
print("Resultado después del entrenamiento:")
print(output)
