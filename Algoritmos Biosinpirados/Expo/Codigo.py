import numpy as np
import matplotlib.pyplot as plt

def sphere_function(x):
    return np.sum(x**2)# Función objetivo a minimizar

class GSA:
    def __init__(self, 
                 pop_size=30,       # Tamaño de la población (número de agentes)
                 dim=2,            # Dimensión del problema
                 max_iter=50,      # Número máximo de iteraciones
                 G0=100,           # Constante G inicial
                 alpha=20,         # Parámetro para decrecer G
                 lb=-10,           # Límite inferior de búsqueda
                 ub=10):           # Límite superior de búsqueda
        
        self.pop_size = pop_size
        self.dim = dim
        self.max_iter = max_iter
        self.G0 = G0
        self.alpha = alpha
        self.lb = lb
        self.ub = ub
        
        # Inicializar posiciones de los agentes de forma aleatoria
        self.positions = np.random.uniform(lb, ub, (pop_size, dim))
        
        # Inicializar velocidades de los agentes en cero
        self.velocities = np.zeros((pop_size, dim))
        
        # Se inicializa el arreglo para almacenar la mejor aptitud en cada iteración
        self.best_values = []
        
        # Se inicializa la mejor posición y el mejor valor encontrados hasta el momento
        self.best_position = None
        self.best_fitness = float('inf')
        
    def mass_calculation(self, fitness):
        # Se normaliza el fitness para calcular la masa
        
        worst = np.max(fitness)#peor agente
        best = np.min(fitness)#mejor agente

        # Para evitar división entre cero
        if worst == best:
            worst += 1e-30
        
        # Normalización lineal de los valores de fitness
        m = (fitness - worst) / (best - worst)
        
        mass = np.abs(m) / np.sum(np.abs(m))
        
        return mass
    
    def update_G(self, iteration):        
        return self.G0 * np.exp(-self.alpha * iteration / self.max_iter)#G disminuye de forma exponencial.
    
    def optimize(self, objective_function):
        for t in range(self.max_iter):
            # Calcular el valor de la función objetivo para cada agente
            fitness = np.array([objective_function(self.positions[i]) for i in range(self.pop_size)])
            
            # Determinar la mejor solución de la población actual
            min_fitness_idx = np.argmin(fitness)
            if fitness[min_fitness_idx] < self.best_fitness:
                self.best_fitness = fitness[min_fitness_idx]
                self.best_position = self.positions[min_fitness_idx].copy()
            
            # Guardamos el mejor valor de esta iteración
            self.best_values.append(self.best_fitness)
            
            # Calcular la masa de cada agente
            M = self.mass_calculation(fitness)
            
            # Actualizar la constante G
            G = self.update_G(t)
            
            # Inicializar aceleraciones en cero
            accelerations = np.zeros((self.pop_size, self.dim))
            
            # Para cada agente, calcular la fuerza neta ejercida por los demás
            for i in range(self.pop_size):
                # Vector de fuerza acumulada
                force_total = np.zeros(self.dim)
                
                for j in range(self.pop_size):
                    if i != j:
                        # Distancia euclidiana entre agentes
                        dist = np.linalg.norm(self.positions[j] - self.positions[i])
                        
                        # Para evitar divisiones entre cero
                        if dist < 1e-30: #valor muy cercano a 0
                            dist = 1e-30
                        
                        # Direccion de la fuerza desde i a j
                        direction = self.positions[j] - self.positions[i]
                        
                        # Calcular la magnitud de la fuerza
                        F = G * (M[i] * M[j]) / (dist + 1e-30)
                        
                        # Acumular la fuerza
                        force_total += np.random.rand() * F * direction / dist
                
                # Calcular la aceleración del agente i
                if M[i] < 1e-30:
                    M[i] = 1e-30
                accelerations[i] = force_total / M[i]
            
            # Actualizar velocidades y posiciones de los agentes
            # v(t+1) = rand * v(t) + a(t)
            # x(t+1) = x(t) + v(t+1)
            self.velocities = np.random.rand(self.pop_size, self.dim) * self.velocities + accelerations
            self.positions += self.velocities
            
            # Control de límites (para que las posiciones se mantengan en [lb, ub])
            self.positions = np.clip(self.positions, self.lb, self.ub)
        
        return self.best_position, self.best_fitness

# ============================
# Ejecución del GSA de ejemplo
# ============================

if __name__ == "__main__":
    # Definir hiperparámetros
    pop_size = 30
    dim = 2
    max_iter = 100
    lb = -5
    ub = 5
    
    # Crear instancia de GSA
    gsa_optimizer = GSA(pop_size=pop_size,
                        dim=dim,
                        max_iter=max_iter,
                        G0=100,
                        alpha=20,
                        lb=lb,
                        ub=ub)
    
    # Optimizar la función esfera
    best_position, best_fitness = gsa_optimizer.optimize(sphere_function)
    
    print("Mejor posición encontrada:", best_position)
    print("Mejor valor (fitness):", best_fitness)
    
    # Graficar la evolución del mejor fitness
    plt.figure(figsize=(8, 5))
    plt.plot(gsa_optimizer.best_values, 'b-', label='Mejor valor encontrado')
    plt.title("Evolución del mejor valor (GSA)")
    plt.xlabel("Iteración")
    plt.ylabel("Valor de la función objetivo")
    plt.legend()
    plt.grid(True)
    plt.show()
