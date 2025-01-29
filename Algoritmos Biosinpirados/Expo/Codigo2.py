import numpy as np
import matplotlib.pyplot as plt

def sphere_function(x):
    return np.sum(x**2)

class GSA:
    def __init__(self, 
                 pop_size=30,      
                 dim=2,           
                 max_iter=50,     
                 G0=100,          
                 alpha=20,        
                 lb=-10,          
                 ub=10):         
        
        self.pop_size = pop_size
        self.dim = dim
        self.max_iter = max_iter
        self.G0 = G0
        self.alpha = alpha
        self.lb = lb
        self.ub = ub
        
        self.positions = np.random.uniform(lb, ub, (pop_size, dim))
        self.velocities = np.zeros((pop_size, dim))
        self.best_values = []
        self.best_position = None
        self.best_fitness = float('inf')
        self.trajectories = []  # Para almacenar las trayectorias de los agentes
        
    def mass_calculation(self, fitness):
        worst = np.max(fitness)
        best = np.min(fitness)
        if worst == best:
            worst += 1e-30
        m = (fitness - worst) / (best - worst)
        mass = np.abs(m) / np.sum(np.abs(m))
        return mass
    
    def update_G(self, iteration):        
        return self.G0 * np.exp(-self.alpha * iteration / self.max_iter)
    
    def optimize(self, objective_function):
        for t in range(self.max_iter):
            # Guardar las posiciones actuales de los agentes para las trayectorias
            self.trajectories.append(self.positions.copy())
            
            fitness = np.array([objective_function(self.positions[i]) for i in range(self.pop_size)])
            min_fitness_idx = np.argmin(fitness)
            if fitness[min_fitness_idx] < self.best_fitness:
                self.best_fitness = fitness[min_fitness_idx]
                self.best_position = self.positions[min_fitness_idx].copy()
            self.best_values.append(self.best_fitness)
            
            M = self.mass_calculation(fitness)
            G = self.update_G(t)
            accelerations = np.zeros((self.pop_size, self.dim))
            
            for i in range(self.pop_size):
                force_total = np.zeros(self.dim)
                for j in range(self.pop_size):
                    if i != j:
                        dist = np.linalg.norm(self.positions[j] - self.positions[i])
                        if dist < 1e-30:
                            dist = 1e-30
                        direction = self.positions[j] - self.positions[i]
                        F = G * (M[i] * M[j]) / (dist + 1e-30)
                        force_total += np.random.rand() * F * direction / dist
                if M[i] < 1e-30:
                    M[i] = 1e-30
                accelerations[i] = force_total / M[i]
            
            self.velocities = np.random.rand(self.pop_size, self.dim) * self.velocities + accelerations
            self.positions += self.velocities
            self.positions = np.clip(self.positions, self.lb, self.ub)
        
        # Agregar las posiciones finales
        self.trajectories.append(self.positions.copy())
        return self.best_position, self.best_fitness

# ============================
# Graficar las trayectorias
# ============================

if __name__ == "__main__":
    pop_size = 30
    dim = 2
    max_iter = 50
    lb = -5
    ub = 5
    
    gsa_optimizer = GSA(pop_size=pop_size,
                        dim=dim,
                        max_iter=max_iter,
                        G0=100,
                        alpha=20,
                        lb=lb,
                        ub=ub)
    
    best_position, best_fitness = gsa_optimizer.optimize(sphere_function)
    
    print("Mejor posición encontrada:", best_position)
    print("Mejor valor (fitness):", best_fitness)
    
    # Extraer las trayectorias
    trajectories = np.array(gsa_optimizer.trajectories)
    
    # Graficar las trayectorias
    plt.figure(figsize=(10, 7))
    for i in range(pop_size):
        agent_trajectory = trajectories[:, i, :]
        plt.plot(agent_trajectory[:, 0], agent_trajectory[:, 1], marker='o', markersize=2, label=f"Agente {i+1}" if i < 5 else "")  # Etiquetamos solo los primeros 5 agentes para no saturar el gráfico
    
    plt.scatter(best_position[0], best_position[1], color='red', label="Mejor posición", zorder=5)
    plt.title("Trayectorias de los agentes (GSA)")
    plt.xlabel("Dimensión X")
    plt.ylabel("Dimensión Y")
    plt.legend(loc='best', fontsize=8)
    plt.grid(True)
    plt.show()
