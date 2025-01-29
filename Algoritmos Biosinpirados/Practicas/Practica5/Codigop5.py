import numpy as np
import random

# Matriz de distancias entre ciudades
M = 2 * np.ones([11, 11])
M[1][3] = 1; M[3][5] = 1; M[5][7] = 1; M[7][9] = 1
M[9][2] = 1; M[2][4] = 1; M[4][6] = 1; M[6][8] = 1
M[8][10] = 1

# Definir parámetros del algoritmo genético
NUM_CITIES = 10
POPULATION_SIZE = 100
NUM_GENERATIONS = 500
MUTATION_RATE = 0.1

# Función de evaluación: Calcula la distancia total de una ruta
def fitness(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += M[tour[i]][tour[i + 1]]
    total_distance += M[tour[-1]][tour[0]]  # Volver a la ciudad inicial
    return total_distance

# Genera una población inicial aleatoria
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        tour = list(range(1, NUM_CITIES + 1))
        random.shuffle(tour)
        population.append(tour)
    return population

# Selección por torneo: Selecciona el mejor entre dos soluciones aleatorias
def tournament_selection(population):
    tournament = random.sample(population, 2)
    fittest = min(tournament, key=fitness)
    return fittest

# Cruce por orden (Order Crossover - OX)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(NUM_CITIES), 2))
    child = [None] * NUM_CITIES
    child[start:end] = parent1[start:end]

    ptr = 0
    for city in parent2:
        if city not in child:
            while child[ptr] is not None:
                ptr += 1
            child[ptr] = city

    return child

# Mutación: Intercambia dos ciudades al azar
def mutate(tour):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NUM_CITIES), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Reemplazo: Reemplaza la población actual con la nueva generación
def replace_population(population, new_population):
    population[:] = new_population

# Función principal para el algoritmo genético
def genetic_algorithm():
    population = initialize_population()
    
    for generation in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        # Reemplazar la población con la nueva generación
        replace_population(population, new_population)

        # Mostrar la mejor solución cada 100 generaciones
        if generation % 100 == 0:
            best_tour = min(population, key=fitness)
            best_fitness = fitness(best_tour)
            print(f"Generación {generation}: Mejor distancia = {best_fitness}, Mejor tour = {best_tour}")

    # Resultado final
    best_tour = min(population, key=fitness)
    best_fitness = fitness(best_tour)
    print(f"\nMejor solución encontrada: Distancia = {best_fitness}, Tour = {best_tour}")
    return best_tour, best_fitness

# Ejecutar el algoritmo genético
best_tour, best_fitness = genetic_algorithm()
