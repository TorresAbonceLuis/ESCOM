import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

# Cargar y preparar los datos
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Crear la función de predicción
def make_prediction():
    sample = [[5.1, 3.5, 1.4, 0.2]]  # Un ejemplo de entrada (puedes cambiar esto)
    prediction = model.predict(sample)
    messagebox.showinfo("Predicción", f"La predicción del modelo es: {iris.target_names[prediction][0]}")

# Crear la función de ayuda
def show_help():
    help_text = ("Esta aplicación utiliza un modelo de clasificación entrenado "
                 "con el conjunto de datos de Iris. Al hacer clic en el botón 'EMPEZAR', "
                 "se realiza una predicción usando una muestra de datos predefinida. "
                 "También puedes generar una matriz de confusión y visualizar las curvas de aprendizaje.")
    messagebox.showinfo("Ayuda", help_text)

# Crear la función para mostrar la matriz de confusión
def show_confusion_matrix():
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.show()

root = tk.Tk()
root.title("Aplicación de ML con scikit-learn")

start_button = tk.Button(root, text="EMPEZAR", command=make_prediction)
start_button.pack(pady=10)

conf_matrix_button = tk.Button(root, text="Matriz de Confusión", command=show_confusion_matrix)
conf_matrix_button.pack(pady=10)

help_button = tk.Button(root, text="AYUDA", command=show_help)
help_button.pack(pady=10)

root.mainloop()


