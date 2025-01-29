import numpy as np
from population import Population
from colorama import Fore, Back, Style, init
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
init(autoreset=True)

X = np.linspace(-5.12, 5.12, 100)
Y = np.linspace(-5.12, 5.12, 100)
Z = np.linspace(-5.12, 5.12, 100)
X, Y, Z = np.meshgrid(X, Y, Z)

def info(_population):
    i = 0
    for _indiv_i in _population.individuals:
        X, Y, Z = _indiv_i.decode_chromosome_rastrigin(lim_a, lim_b, n_chains)
        print(
            Back.LIGHTBLACK_EX + Fore.WHITE + Style.BRIGHT + f"individual: {X:.3f} {Y:.3f} {Z:.3f}",
            f"fitness: {Fore.MAGENTA}{_indiv_i.fitness:.3f}",
            f"x:{Fore.GREEN}{X:.3f} y:{Fore.GREEN}{Y:.3f} z:{Fore.GREEN}{Z:.3f}",
            Style.RESET_ALL
        )
        i += 1

    X, Y, Z = sorted(_population.individuals, key=lambda x: x.fitness, reverse=False)[0].decode_chromosome_rastrigin(lim_a, lim_b, n_chains)
    print(
        Back.LIGHTBLACK_EX + Fore.WHITE + Style.BRIGHT + f"Best solution X={Fore.GREEN}{X:.3f} Y={Fore.GREEN}{Y:.3f} Z={Fore.GREEN}{Z:.3f}",
        Style.RESET_ALL
    )
    print("rastrigin(X, Y, Z) =", rastrigin(X, Y, Z))
    return(X,Y,Z)

def rastrigin(X, Y, Z):
    return (X**2 - 10 * np.cos(2 * np.pi * X)) + (Y**2 - 10 * np.cos(2 * np.pi * Y)) + (Z**2 - 10 * np.cos(2 * np.pi * Z)) + 30

if __name__ == '__main__':
    size_population = 14
    chromosome_length = 30
    mutation_probability = .75
    max_number_generations = 100
    crossover_point = int((chromosome_length)/2)
    n_chains = 2**int(chromosome_length/3)

    lim_a = -5.12
    lim_b = 5.12

    _population = Population(size_population, mutation_probability, chromosome_length, crossover_point)

    latestINFO = (99,99,99)

    for i in range(0, max_number_generations):
        _population.evaluate_population_rastrigin(rastrigin, lim_a, lim_b, n_chains)
        _population.create_selection_wheel()
        latestINFO = info(_population)
        F_n = _population.next_generation()
        _population.individuals.clear()
        _population.individuals[:] = F_n[:]
        F_n.clear()
    
    X = np.linspace(-5.12, 5.12, 100)
    Y = np.linspace(-5.12, 5.12, 100)
    X, Y = np.meshgrid(X, Y)
    Z = rastrigin(X, Y, np.zeros_like(X))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5, label='Rastrigin Function')

    ax.scatter(latestINFO[0], latestINFO[1], rastrigin(*latestINFO), color='red', marker='o', s=100, label='Best solution')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.show()
