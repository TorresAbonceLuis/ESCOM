import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

clientes = pd.read_csv("datos_clientes.csv")

buenos = clientes[clientes["cumplio"]==1]
malos = clientes[clientes["cumplio"]==0]

print(f'Cumplio con el pago\n{buenos}\nNo cumplio con el pago\n{malos}')

plt.scatter(buenos["edad"], buenos["credito"],
            marker="*", s=150, color="green",
            label="Sí pagó (Clase: 1)")

plt.scatter(malos["edad"], malos["credito"],
            marker="*", s=150, color="brown", 
            label="No pagó (Clase: 0)")

plt.ylabel("Monto del crédito")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1, 0.2)) 
plt.show()