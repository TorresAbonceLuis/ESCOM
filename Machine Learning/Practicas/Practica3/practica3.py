import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate 

musica = pd.read_csv("datos_musica.csv", encoding='ISO-8859-1')

# Separar los datos por género
genero0 = musica[musica["Género Musical"]==0]
genero1 = musica[musica["Género Musical"]==1]
genero2 = musica[musica["Género Musical"]==2]
genero3 = musica[musica["Género Musical"]==3]



# Graficar los datos
plt.scatter(genero0["Duración de la Canción"], genero0["Número de Reproducciones"], marker="*", s=150, color="green", label="Género 0")
plt.scatter(genero1["Duración de la Canción"], genero1["Número de Reproducciones"], marker="*", s=150, color="red", label="Género 1")
plt.scatter(genero2["Duración de la Canción"], genero2["Número de Reproducciones"], marker="*", s=150, color="pink", label="Género 2")
plt.scatter(genero3["Duración de la Canción"], genero3["Número de Reproducciones"], marker="*", s=150, color="gray", label="Género 3")



plt.ylabel("Número de Reproducciones")
plt.xlabel("Duración de la Canción")
plt.legend(bbox_to_anchor=(1, 0.2)) 
#plt.show()
for genero in range(4):
    cantidad = len(musica[musica["Género Musical"]==genero])
    #print(f"Cantidad de canciones en el género {genero}: {cantidad}")

# Preparar los datos para el clasificador
datos = musica[["Duración de la Canción", "Número de Reproducciones"]]
clase = musica["Género Musical"]

escalador = preprocessing.MinMaxScaler()

datos = escalador.fit_transform(datos)

#print(datos) 

clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador15 = KNeighborsClassifier(n_neighbors=15)
clasificador.fit(datos, clase)
clasificador15.fit(datos, clase)

# 10 Iteraciones
# Definir las métricas que deseas calcular 
scoring = ['accuracy', 'precision_macro','recall_macro', 'f1_macro'] 
scores10 = cross_validate(clasificador, datos, clase, cv=10, scoring=scoring)
'''
# k = 3
print('k = 3')
print('------Metricas-----')
print("Accuracy:", scores10['test_accuracy'].mean()) 
print("Precision:", scores10['test_precision_macro'].mean()) 
print("Recall:", scores10['test_recall_macro'].mean()) 
print("F-score:", scores10['test_f1_macro'].mean()) 
print('-----Scores10-----')
print(scores10.keys())
print(scores10)
'''
# 10 Iteraciones
# Definir las métricas que deseas calcular 
scoring = ['accuracy', 'precision_macro','recall_macro', 'f1_macro'] 
scores10 = cross_validate(clasificador15, datos, clase, cv=10, scoring=scoring)  
# k = 15
'''	
print('k = 15')
print('------Metricas-----')
print("Accuracy:", scores10['test_accuracy'].mean()) 
print("Precision:", scores10['test_precision_macro'].mean()) 
print("Recall:", scores10['test_recall_macro'].mean()) 
print("F-score:", scores10['test_f1_macro'].mean()) 
print('-----Scores10-----')
print(scores10.keys())
print(scores10)
'''	

# Crear un nuevo objeto
nuevo_objeto = [[300, 50000]]  # Duración de la Canción: 300, Número de Reproducciones: 50000

# Escalar los datos del nuevo objeto
nuevo_objeto_escalado = escalador.transform(nuevo_objeto)

# Realizar una predicción para el nuevo objeto
prediccion = clasificador.predict(nuevo_objeto_escalado)
#probabilidades = clasificador.predict_proba(nuevo_objeto_escalado)
probabilidades = clasificador15.predict_proba(nuevo_objeto_escalado)

# Imprimir la clase asignada y las probabilidades por clase
print(f"Clase asignada para el nuevo objeto: {prediccion[0]}")
print(f"Probabilidades por clase: {probabilidades[0]}")

# Graficar los 200 objetos y el nuevo objeto
plt.scatter(datos[:, 0], datos[:, 1], c=clase)
plt.scatter(nuevo_objeto_escalado[0, 0], nuevo_objeto_escalado[0, 1], color="green", marker="P", s=150,label="Nuevo Objeto")
plt.ylabel("Número de Reproducciones")
plt.xlabel("Duración de la Canción")
#plt.show()

x_min, x_max = datos[:, 0].min() - 1, datos[:, 0].max() + 1
y_min, y_max = datos[:, 1].min() - 1, datos[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Usar el clasificador para predecir la clase de cada punto en la malla
Z = clasificador.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Dibujar la malla usando colores para indicar la clase de cada punto
plt.contourf(xx, yy, Z, alpha=0.8)

# Dibujar los puntos de datos
plt.scatter(datos[:, 0], datos[:, 1], c=clase, edgecolor='k')

# Dibujar el nuevo objeto
plt.scatter(nuevo_objeto_escalado[0, 0], nuevo_objeto_escalado[0, 1], color="green", marker="P", s=150,label="Nuevo Objeto")

plt.ylabel("Número de Reproducciones")
plt.xlabel("Duración de la Canción")
plt.show()