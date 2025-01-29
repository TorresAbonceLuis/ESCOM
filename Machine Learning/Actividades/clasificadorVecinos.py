import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Generar datos sintéticos
np.random.seed(0)
edad = np.random.randint(18, 61, 200)
credito = np.random.randint(3000, 1000001, 200)
cumplio = np.random.randint(0, 2, 200)

# Crear DataFrame
clientes = pd.DataFrame({'edad': edad, 'credito': credito, 'cumplio': cumplio})
clientes.to_csv('clientes.csv', index=False)

# Filtrar clientes que pagaron y que no pagaron
clientes_buenos = clientes[clientes['cumplio'] == 1]
clientes_malos = clientes[clientes['cumplio'] == 0]

# Contar clientes que pagaron y que no pagaron
num_buenos = len(clientes_buenos)
num_malos = len(clientes_malos)

# Normalizar datos
datos = clientes [["edad", "credito"]]
clase = clientes ["cumplio"]

escalador = preprocessing.MinMaxScaler()
datos = escalador.fit_transform(datos)

clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador.fit(datos, clase)

edad = 53
monto = 350000

#Escalar los datos del nuevo solicitante
solicitante = escalador.transform([[edad, monto]])

#Calcular clase y probabilidades
print("Clase:", clasificador.predict(solicitante))
print("Probabilidades por clase",
      clasificador.predict_proba(solicitante))

#Código para graficar
plt.scatter(buenos["edad"], buenos["credito"],
            marker="*", s=150, color="skyblue", label="Sí pagó (Clase: 1)")
plt.scatter(malos["edad"], malos["credito"],
            marker="*", s=150, color="red", label="No pagó (Clase: 0)")
plt.scatter(edad, monto, marker="P", s=250, color="green", label="Solicitante") 
plt.ylabel("Monto del crédito")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1, 0.3))
plt.show()