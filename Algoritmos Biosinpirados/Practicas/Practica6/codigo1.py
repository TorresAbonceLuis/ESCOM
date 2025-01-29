import numpy as np

# Define la función de Schwefel en 4 dimensiones
def schwefel(x):
    return 418.9829 * len(x) - sum(x * np.sin(np.sqrt(np.abs(x))))

# Parámetros del PSO
num_particles = 30        # Número de partículas
num_dimensions = 4        # Dimensiones del problema
max_iterations = 100      # Número de iteraciones

# Limites de búsqueda (según la función de Schwefel, [-500, 500] es adecuado)
bounds = (-500, 500)

# Parámetros de PSO
w = 0.5          # Factor de inercia
c1 = 1.5         # Coeficiente cognitivo
c2 = 1.5         # Coeficiente social

# Inicialización de las partículas
particles = np.random.uniform(bounds[0], bounds[1], (num_particles, num_dimensions))
velocities = np.random.uniform(-1, 1, (num_particles, num_dimensions))
personal_best = particles.copy()
personal_best_scores = np.array([schwefel(p) for p in particles])
global_best = personal_best[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# Optimización PSO
for iteration in range(max_iterations):
    for i in range(num_particles):
        # Evaluación de la función objetivo
        score = schwefel(particles[i])

        # Actualización del mejor valor personal
        if score < personal_best_scores[i]:
            personal_best[i] = particles[i]
            personal_best_scores[i] = score

        # Actualización del mejor valor global
        if score < global_best_score:
            global_best = particles[i]
            global_best_score = score

    # Actualización de la velocidad y posición de cada partícula
    for i in range(num_particles):
        r1, r2 = np.random.rand(), np.random.rand()
        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (personal_best[i] - particles[i])
            + c2 * r2 * (global_best - particles[i])
        )

        # Actualización de posición de la partícula
        particles[i] += velocities[i]

        # Limitar las partículas dentro de los límites
        particles[i] = np.clip(particles[i], bounds[0], bounds[1])


print("Mejor posición encontrada:", global_best)
print("Mejor valor de la función Schwefel:", global_best_score)
