import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LambdaCallback
import matplotlib.pyplot as plt

# Cargar y preparar los datos de ejemplo
def load_data():
    cali = fetch_california_housing()
    inputs = cali.data
    targets = cali.target.reshape(-1, 1)
    
    # Estandarizar los datos
    scaler = StandardScaler()
    inputs = scaler.fit_transform(inputs)
    
    global inputs_loaded, targets_loaded
    inputs_loaded, targets_loaded = inputs, targets
    messagebox.showinfo("Datos", "Datos cargados exitosamente.")
    
    # Habilitar el botón de entrenar
    train_button.config(state=tk.NORMAL)

# Crear la red neuronal
def create_network(hidden_layer_size, num_hidden_layers, optimizer):
    model = Sequential()
    model.add(Dense(hidden_layer_size, input_dim=8, activation='tanh'))  # 8 características de entrada
    for _ in range(num_hidden_layers - 1):
        model.add(Dense(hidden_layer_size, activation='tanh'))
    model.add(Dense(1, activation='linear'))  # Salida única para regresión
    model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mse'])
    return model

# Callback para mostrar el progreso del entrenamiento en la terminal
def on_epoch_end(epoch, logs):
    print(f"Epoch {epoch+1}: loss={logs['loss']:.4f}, mse={logs['mse']:.4f}, val_loss={logs['val_loss']:.4f}, val_mse={logs['val_mse']:.4f}")

# Entrenar la red
def train_network():
    hidden_layer_size = int(hidden_layer_size_entry.get())
    num_hidden_layers = int(num_hidden_layers_entry.get())
    optimizer_name = optimizer_combobox.get()
    
    optimizers = {
        'Levenberg-Marquardt (trainlm)': Adam(learning_rate=0.001),
        'Regularización Bayesiana (trainbr)': Adam(learning_rate=0.001),
        'Gradiente Conjugado Escalado (trainscg)': Adam(learning_rate=0.001)
    }
    
    optimizer = optimizers[optimizer_name]
    global model
    model = create_network(hidden_layer_size, num_hidden_layers, optimizer)
    
    global inputs, targets, history
    inputs, targets = inputs_loaded, targets_loaded
    
    # Dividir los datos en entrenamiento, validación y prueba (70%, 15%, 15%)
    X_train, X_temp, y_train, y_temp = train_test_split(inputs, targets, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    epoch_end_callback = LambdaCallback(on_epoch_end=on_epoch_end)
    
    history = model.fit(X_train, y_train, epochs=100, validation_data=(X_val, y_val), verbose=0, callbacks=[epoch_end_callback])
    
    global performance, outputs, errors
    outputs = model.predict(inputs)
    errors = targets - outputs
    performance = model.evaluate(X_test, y_test, verbose=0)
    
    messagebox.showinfo("Entrenamiento", f"Entrenamiento completado.\nRendimiento: {performance[1]:.4f}")
    
    # Habilitar el botón de probar
    test_button.config(state=tk.NORMAL)

def plot_performance():
    global history
    plt.figure()
    plt.plot(history.history['mse'], label='MSE Entrenamiento')
    plt.plot(history.history['val_mse'], label='MSE Validación')
    plt.title('Rendimiento del entrenamiento')
    plt.xlabel('Epoch')
    plt.ylabel('MSE')
    plt.legend()
    plt.show()

def plot_train_state():
    global history
    plt.figure()
    plt.plot(history.history['loss'], label='Loss Entrenamiento')
    plt.plot(history.history['val_loss'], label='Loss Validación')
    plt.title('Estado del entrenamiento')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def plot_fit():
    global targets, outputs
    plt.figure()
    plt.plot(targets.flatten(), label='Targets')
    plt.plot(outputs.flatten(), label='Outputs')
    plt.title('Ajuste del modelo')
    plt.xlabel('Muestras')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()

def plot_regression():
    global targets, outputs
    plt.figure()
    plt.scatter(targets.flatten(), outputs.flatten())
    plt.plot([min(targets.flatten()), max(targets.flatten())], [min(targets.flatten()), max(targets.flatten())], 'r--')
    plt.title('Regresión')
    plt.xlabel('Valores reales')
    plt.ylabel('Predicciones')
    plt.show()

def plot_err_hist():
    global errors
    plt.figure()
    plt.hist(errors.flatten(), bins=20)
    plt.title('Histograma de Errores')
    plt.show()

def view_network():
    global model
    if model:
        model.summary()
    else:
        messagebox.showerror("Error", "Primero entrene la red.")
    
    # Habilitar el botón de mostrar gráficas
    plot_button.config(state=tk.NORMAL)

def test_network():
    global model, inputs, targets
    if model:
        outputs = model.predict(inputs)
        errors = targets - outputs
        plt.figure()
        plt.hist(errors.flatten(), bins=20)
        plt.title('Histograma de Errores')
        plt.show()
        
        performance = model.evaluate(inputs, targets, verbose=0)
        messagebox.showinfo("Rendimiento", f"Rendimiento de la red: {performance[1]:.4f}")
    else:
        messagebox.showerror("Error", "Primero entrene la red.")
    
    # Habilitar el botón de diagrama de red
    view_button.config(state=tk.NORMAL)

# Interfaz gráfica
root = tk.Tk()
root.title("Red Neuronal")

tk.Label(root, text="Número de neuronas en la capa oculta:").grid(row=0, column=0, padx=10, pady=10)
hidden_layer_size_entry = tk.Entry(root)
hidden_layer_size_entry.grid(row=0, column=1, padx=10, pady=10)
hidden_layer_size_entry.insert(0, "10")  # Valor predeterminado

tk.Label(root, text="Número de capas ocultas:").grid(row=1, column=0, padx=10, pady=10)
num_hidden_layers_entry = tk.Entry(root)
num_hidden_layers_entry.grid(row=1, column=1, padx=10, pady=10)
num_hidden_layers_entry.insert(0, "5")  # Valor predeterminado

tk.Label(root, text="Algoritmo de entrenamiento:").grid(row=2, column=0, padx=10, pady=10)
optimizer_combobox = ttk.Combobox(root, values=["Levenberg-Marquardt (trainlm)", "Regularización Bayesiana (trainbr)", "Gradiente Conjugado Escalado (trainscg)"])
optimizer_combobox.grid(row=2, column=1, padx=10, pady=10)
optimizer_combobox.set("Regularización Bayesiana (trainbr)")  # Valor predeterminado

load_button = tk.Button(root, text="Cargar Datos", command=load_data)
load_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

train_button = tk.Button(root, text="Entrenar Red", command=train_network, state=tk.DISABLED)
train_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

test_button = tk.Button(root, text="Probar Red", command=test_network, state=tk.DISABLED)
test_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

view_button = tk.Button(root, text="Vista del Diagrama de Red", command=view_network, state=tk.DISABLED)
view_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

plot_button = tk.Button(root, text="Mostrar Gráficas", command=lambda: [plot_performance(), plot_train_state(), plot_fit(), plot_regression(), plot_err_hist()], state=tk.DISABLED)
plot_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
