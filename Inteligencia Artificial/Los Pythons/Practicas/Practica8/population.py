import random
from individual import Individual

class Population:
    def __init__(self, size_population, mutation_probability, chromosome_length, crossover_point):
        # Initialize population parameters
        self.size_population = size_population
        self.generation_number = 0
        self.mutation_probability = mutation_probability
        self.crossover_point = crossover_point
        self.individuals = []

        # Create initial population with random individuals
        for _ in range(self.size_population):
            self.individuals.append(Individual(chromosome_length))

    def evaluate_population(self, fitness_function, lim_a, lim_b, n_chains):
        # Evaluate the fitness of each individual in the population
        for individual in self.individuals:
            individual.set_fitness(fitness_function, lim_a, lim_b, n_chains)

    def evaluate_population_rastrigin(self, fitness_function, lim_a, lim_b, n_chains):
        # Evaluate the fitness of each individual in the population (Rastrigin function)
        for individual in self.individuals:
            individual.set_fitness_rastrigin(fitness_function, lim_a, lim_b, n_chains)

    def create_selection_wheel(self):
        # Create a selection wheel based on the fitness of individuals
        total_fitness = sum(abs(individual.fitness) for individual in self.individuals)
        selection_wheel = [abs(individual.fitness) / total_fitness for individual in self.individuals]
        return selection_wheel

    def select_parents(self):
        # Randomly select parents based on the selection wheel
        return random.choices(self.individuals, weights=self.create_selection_wheel())[0]

    def next_generation(self):
        # Generate the next generation using genetic operations
        next_generation = []
        
        # Elitism: Keep the two best individuals from the current generation
        elitism = sorted(self.individuals, key=lambda x: x.fitness, reverse=False)
        next_generation.extend(elitism[:2])

        # Apply genetic operations to create the rest of the next generation
        for _ in range((self.size_population - 2) // 2):
            parent_1 = self.select_parents()
            parent_2 = self.select_parents()
            
            # Reproduction, crossover, and mutation
            descendant_1, descendant_2 = parent_1.reproduction(parent_2, self.crossover_point)
            descendant_1.mutate(self.mutation_probability)
            descendant_2.mutate(self.mutation_probability)
            
            next_generation.extend([descendant_1, descendant_2])

        return next_generation
