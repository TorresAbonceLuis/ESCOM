# Heurística greedy para el problema de cambio de monedas (CMP)
def cambio_greedy(monedas, cantidad):
    monedas.sort(reverse=True)  # Ordenar las monedas de mayor a menor valor
    cambio = []
    total_monedas = 0

    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            cambio.append(moneda)
            total_monedas += 1

    if cantidad != 0:
        return None, total_monedas  # Si no es posible dar el cambio exacto
    return cambio, total_monedas

# Ejemplo donde el algoritmo greedy falla (solución subóptima)
monedas_fallo = [25, 10, 5, 1]
cantidad_fallo = 30  # Greedy seleccionará 25 + 5, pero lo óptimo sería 10 + 10 + 10
resultado_fallo, num_monedas_fallo = cambio_greedy(monedas_fallo, cantidad_fallo)
print("Solución Greedy (Fallo):", resultado_fallo, "Número de monedas:", num_monedas_fallo)  # El resultado óptimo sería [10, 10, 10], 3 monedas.

# Ejemplo donde el algoritmo greedy tiene éxito (solución óptima)
monedas_exito = [25, 10, 5, 1]
cantidad_exito = 37  # Greedy dará 25 + 10 + 1 + 1
resultado_exito, num_monedas_exito = cambio_greedy(monedas_exito, cantidad_exito)
print("Solución Greedy (Éxito):", resultado_exito, "Número de monedas:", num_monedas_exito)  # El resultado correcto esperado es [25, 10, 1, 1], 4 monedas.
