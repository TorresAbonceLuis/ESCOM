def mochila(weights, values, capacidad):
    n = len(weights)
    # Crear una matriz 2D para almacenar el valor máximo en cada capacidad
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]

    # Rellenar la tabla dp
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if weights[i - 1] <= w:
                # Si el peso del objeto actual es menor o igual a la capacidad actual,
                # elegimos entre incluir o no incluir el objeto
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Si el peso del objeto es mayor que la capacidad actual, no lo incluimos
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidad]

# Ejemplos de ejecución
pesos = [1, 2, 3, 4]
valores = [10, 20, 30, 40]
capacidad = 5
print("Valor máximo en la mochila:", mochila(pesos, valores, capacidad))

pesos = [2, 3, 4]
valores = [3, 4, 5]
capacidad = 5
print("Valor máximo en la mochila:", mochila(pesos, valores, capacidad))
