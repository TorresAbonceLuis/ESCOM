def cambio_monedas(monedas, cantidad):
    # Crear una lista para almacenar el número mínimo de monedas para cada cantidad
    dp = [float('inf')] * (cantidad + 1)
    dp[0] = 0  # Se necesitan 0 monedas para la cantidad 0

    # Rellenar la tabla dp
    for i in range(1, cantidad + 1):
        for moneda in monedas:
            if moneda <= i:
                dp[i] = min(dp[i], dp[i - moneda] + 1)

    # Si la cantidad no puede alcanzarse con las monedas disponibles, devolver -1
    return dp[cantidad] if dp[cantidad] != float('inf') else -1

# Ejemplos de ejecución
monedas = [1, 2, 5]
cantidad = 11
print("Número mínimo de monedas:", cambio_monedas(monedas, cantidad))

monedas = [2, 5, 10]
cantidad = 7
print("Número mínimo de monedas:", cambio_monedas(monedas, cantidad))
