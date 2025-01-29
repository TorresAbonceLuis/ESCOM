import ipywidgets as widgets
import math
import random
import numpy as np
from functools import cmp_to_key
from IPython import display as display

# Parámetros generales
L_chromosome = 16  # Longitud del cromosoma (bits)
N_chromosomes = 10  # Número de cromosomas
prob_m = 0.1  # Probabilidad de mutación
a = -20  # Límite inferior del espacio de búsqueda
b = 20  # Límite superior del espacio de búsqueda
crossover_point = L_chromosome // 2  # Punto de cruce
Lwheel = N_chromosomes * 10  # Tamaño de la ruleta
n = 0  # Contador de generaciones

# Inicialización de cromosomas
def random_chromosome():
    return [random.randint(0, 1) for _ in range(L_chromosome)]

# Decodificación de cromosomas binarios a valores reales
def decode_chromosome(chromosome):
    value = 0
    for p in range(L_chromosome):
        value += (2 ** p) * chromosome[-1 - p]
    return a + (b - a) * float(value) / (2**L_chromosome - 1)

# Función de Ackley en 2D
def ackley_function(x, y):
    term1 = -20 * math.exp(-0.2 * math.sqrt(0.5 * (x**2 + y**2)))
    term2 = -math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
    return term1 + term2 + 20 + math.e

# Función de Rastrigin en 3D
def rastrigin_function(x, y, z):
    return 30 + (x**2 - 10 * math.cos(2 * math.pi * x)) + \
           (y**2 - 10 * math.cos(2 * math.pi * y)) + \
           (z**2 - 10 * math.cos(2 * math.pi * z))

# Evaluación de cromosomas para Ackley
def evaluate_ackley_population(population):
    fitness_values = []
    for chrom in population:
        x = decode_chromosome(chrom)
        y = decode_chromosome(chrom)
        fitness = ackley_function(x, y)
        fitness_values.append(fitness)
    return fitness_values

# Evaluación de cromosomas para Rastrigin
def evaluate_rastrigin_population(population):
    fitness_values = []
    for chrom in population:
        x = decode_chromosome(chrom)
        y = decode_chromosome(chrom)
        z = decode_chromosome(chrom)
        fitness = rastrigin_function(x, y, z)
        fitness_values.append(fitness)
    return fitness_values

# Selección por ruleta
def create_wheel(fitness_values):
    max_fitness = max(fitness_values)
    acc = 0
    for fv in fitness_values:
        acc += max_fitness - fv
    fraction = [(max_fitness - fv) / acc for fv in fitness_values]
    
    wheel = []
    pc = 0
    for f in fraction:
        Np = int(f * Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc += 1
    return wheel

# Operador de cruce y mutación
def crossover_and_mutate(parent1, parent2):
    crossover_point = random.randint(1, L_chromosome - 2)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    # Mutación
    for i in range(L_chromosome):
        if random.random() < prob_m:
            offspring1[i] ^= 1
        if random.random() < prob_m:
            offspring2[i] ^= 1

    return offspring1, offspring2

# Creación de la nueva generación
def next_generation(population, fitness_function):
    fitness_values = fitness_function(population)
    population.sort(key=lambda chrom: fitness_function([chrom])[0])
    
    # Selección de los mejores
    new_population = [population[0], population[1]]  # Elitismo

    wheel = create_wheel(fitness_values)
    while len(new_population) < N_chromosomes:
        p1 = random.choice(wheel)
        p2 = random.choice(wheel)
        offspring1, offspring2 = crossover_and_mutate(population[p1], population[p2])
        new_population.append(offspring1)
        new_population.append(offspring2)

    return new_population[:N_chromosomes]

# Botón para avanzar generaciones
def create_button():
    button = widgets.Button(
        description='Next Generation',
        disabled=False,
        button_style='',  # 'success', 'info', 'warning', 'danger'
        tooltip='Next Generation',
        icon='check'  # Icono (FontAwesome)
    )
    return button

# Función para ejecutar la siguiente generación (Ackley)
def next_generation_ackley_callback(b):
    global population_ackley, n
    display.clear_output(wait=True)
    display.display(button_ackley)
    
    population_ackley = next_generation(population_ackley, evaluate_ackley_population)
    n += 1
    
    # Mostrar los mejores cromosomas y el valor de fitness
    best_chrom = population_ackley[0]
    x_best = decode_chromosome(best_chrom)
    y_best = decode_chromosome(best_chrom)
    print(f"Generation {n}: Best solution so far: f({x_best}, {y_best}) = {ackley_function(x_best, y_best)}")

# Función para ejecutar la siguiente generación (Rastrigin)
def next_generation_rastrigin_callback(b):
    global population_rastrigin, n
    display.clear_output(wait=True)
    display.display(button_rastrigin)
    
    population_rastrigin = next_generation(population_rastrigin, evaluate_rastrigin_population)
    n += 1
    
    # Mostrar los mejores cromosomas y el valor de fitness
    best_chrom = population_rastrigin[0]
    x_best = decode_chromosome(best_chrom)
    y_best = decode_chromosome(best_chrom)
    z_best = decode_chromosome(best_chrom)
    print(f"Generation {n}: Best solution so far: f({x_best}, {y_best}, {z_best}) = {rastrigin_function(x_best, y_best, z_best)}")

# Crear el botón para Ackley
button_ackley = create_button()
button_ackley.on_click(next_generation_ackley_callback)

# Crear el botón para Rastrigin
button_rastrigin = create_button()
button_rastrigin.on_click(next_generation_rastrigin_callback)

# Inicialización de las poblaciones
population_ackley = [random_chromosome() for _ in range(N_chromosomes)]
population_rastrigin = [random_chromosome() for _ in range(N_chromosomes)]

# Mostrar el botón para Ackley
display.display(button_ackley)

# Mostrar el botón para Rastrigin
display.display(button_rastrigin)
