# Mochila 0/1 con heurística voraz
class Item:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.ratio = valor / peso

def mochila_greedy(capacidad, items):
    items.sort(key=lambda x: x.ratio, reverse=True)  # Ordenar por valor/peso
    peso_actual = 0
    valor_total = 0
    seleccion = []

    for item in items:
        if peso_actual + item.peso <= capacidad:
            seleccion.append(item)
            peso_actual += item.peso
            valor_total += item.valor

    return valor_total, seleccion

# Ejemplo de donde falla el algoritmo greedy (solución subóptima)
items_fallo = [Item(60, 10), Item(100, 20), Item(120, 30)]  # Ordenado por valor/peso
capacidad_fallo = 50
resultado_fallo, seleccion_fallo = mochila_greedy(capacidad_fallo, items_fallo)
print("Solución Greedy (Fallo):", resultado_fallo)  # Resultado incorrecto: 160, óptimo: 220

# Ejemplo donde el algoritmo greedy tiene éxito (solución óptima)
items_exito = [Item(100, 10), Item(60, 20), Item(120, 30)]
capacidad_exito = 50
resultado_exito, seleccion_exito = mochila_greedy(capacidad_exito, items_exito)
print("Solución Greedy (Éxito):", resultado_exito)  # Resultado correcto esperado: 220
