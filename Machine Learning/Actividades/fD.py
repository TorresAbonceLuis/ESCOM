import numpy as np
import matplotlib.pyplot as plt
# Generar datos sintéticos
np.random.seed(0)
# Grupo 1: alrededor del punto (1, 1)
group1 = np.random.randn(100, 2) + np.array([1, 1])
# Grupo 2: alrededor del punto (4, 4)
group2 = np.random.randn(100, 2) + np.array([4, 4])
# Función discriminante lineal
def linear_discriminant(x, y, coef):
    a, b, c = coef
    return a*x + b*y - c
# Coeficientes de la FD lineal (seleccionados para este ejemplo)
linear_coef = [1, -1, 0]

def quadratic_discriminant(x, y, coef):
    a, b, c, d, e, f = coef
    return a*x**2 + b*y**2 + c*x*y + d*x + e*y - f
quadratic_coef = [1, 1, 0, -5, -5, 8]

def polynomial_discriminant(x, y, coef):
    a, b, c, d, e, f, g, h, i, j = coef
    return (a*x**3 + b*y**3 + c*x**2*y + d*x*y**2 + e*x**2 + f*y**2 + g*x*y + h*x + i*y - j)
polynomial_coef = [0.1, 0.1, 0, 0, -1, -1, 0, 4, 4, 4]
# Crear un grid para visualización
x_values = np.linspace(-2, 7, 400)
y_values = np.linspace(-2, 7, 400)
xx, yy = np.meshgrid(x_values, y_values)
# Evaluar las funciones discriminantes en el grid
zz_linear = linear_discriminant(xx, yy, linear_coef)
zz_quadratic = quadratic_discriminant(xx, yy, quadratic_coef)
zz_polynomial = polynomial_discriminant(xx, yy, polynomial_coef)
# Plotting
plt.figure(figsize=(18, 6))
# Discriminanate Lineal
plt.subplot(1, 3, 1)
plt.contourf(xx, yy, zz_linear, levels=0, alpha=0.2, colors=['blue', 'red'])
plt.scatter(group1[:, 0], group1[:, 1], color='green', label='Group 1')
plt.scatter(group2[:, 0], group2[:, 1], color='purple', label='Group 2')
plt.title('Discriminanate Lineal')
plt.legend()

# Discriminanate Cuadrática
plt.subplot(1, 3, 2)
plt.contourf(xx, yy, zz_quadratic, levels=0, alpha=0.2, colors=['blue', 'red'])
plt.scatter(group1[:, 0], group1[:, 1], color='green', label='Group 1')
plt.scatter(group2[:, 0], group2[:, 1], color='purple', label='Group 2')
plt.title('Discriminanate Cuadrática')
plt.legend()
# Discriminanate Polinomial
plt.subplot(1, 3, 3)
plt.contourf(xx, yy, zz_polynomial, levels=0, alpha=0.2, colors=['blue', 'red'])
plt.scatter(group1[:, 0], group1[:, 1], color='green', label='Group 1')
plt.scatter(group2[:, 0], group2[:, 1], color='purple', label='Group 2')
plt.title('Discriminanate Polinomial')
plt.legend()
plt.show()
