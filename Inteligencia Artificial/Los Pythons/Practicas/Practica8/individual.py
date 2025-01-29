import random

class Individual:
    def __init__(self, chromosome_length, mutation_probability=0.3):
        self.chromosome = random.getrandbits(chromosome_length)
        self.chromosome_length = chromosome_length
        self.fitness = 0
        self.initialize_random_bits(mutation_probability)

    def initialize_random_bits(self, mutation_probability):
        for i in range(self.chromosome_length):
            if random.random() < mutation_probability:
                self.flip_bit(i)

    def flip_bit(self, position):
        self.chromosome ^= (1 << position)

    def decode_chromosome(self, lim_a, lim_b, n_chains):
        return lim_a + (lim_b - lim_a) * self.chromosome / (n_chains - 1)

    def decode_chromosome_rastrigin(self, lim_a, lim_b, n_chains):
        split_point = self.chromosome_length // 3
        left_mask = (2 ** self.chromosome_length - 1) - (2 ** (2 * split_point) - 1)
        right_mask = 2 ** split_point - 1
        center_mask = 2 ** self.chromosome_length - 1

        center_mask ^= left_mask | right_mask

        X = (left_mask & self.chromosome) >> 2 * split_point
        Y = (center_mask & self.chromosome) >> split_point
        Z = (right_mask & self.chromosome)
        
        return (
            lim_a + (lim_b - lim_a) * X / (n_chains - 1),
            lim_a + (lim_b - lim_a) * Y / (n_chains - 1),
            lim_a + (lim_b - lim_a) * Z / (n_chains - 1),
        )

    def set_fitness(self, fitness_function, lim_a, lim_b, n_chains):
        self.fitness = fitness_function(self.decode_chromosome(lim_a, lim_b, n_chains))

    def set_fitness_rastrigin(self, fitness_function, lim_a, lim_b, n_chains):
        X, Y, Z = self.decode_chromosome_rastrigin(lim_a, lim_b, n_chains)
        self.fitness = fitness_function(X, Y, Z)

    def reproduction(self, other, crossover_point):
        left_mask = (2 ** self.chromosome_length - 1) - (2 ** (self.chromosome_length - crossover_point) - 1)
        right_mask = 2 ** crossover_point - 1

        d1_chromosome = (left_mask & self.chromosome) | (right_mask & other.chromosome)
        d2_chromosome = (left_mask & other.chromosome) | (right_mask & self.chromosome)

        descendant_1 = Individual(self.chromosome_length)
        descendant_2 = Individual(self.chromosome_length)

        descendant_1.set_chromosome(d1_chromosome)
        descendant_2.set_chromosome(d2_chromosome)

        return descendant_1, descendant_2

    def mutate(self, mutation_probability):
        if random.random() < mutation_probability:
            position = random.randrange(self.chromosome_length)
            self.flip_bit(position)

    def set_chromosome(self, chromosome):
        self.chromosome = chromosome
