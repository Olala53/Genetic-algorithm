import random

def objective_function(chromosome):
    return sum(chromosome)

def fitness_evaluation(chromosome):
    return 1 / (1 + objective_function(chromosome))

def initialize_population(population_size, chromosome_size):
    return [[random.randint(0, 1) for _ in range(chromosome_size)] for _ in range(population_size)]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome, mutation_probability):
    for i in range(len(chromosome)):
        if random.random() < mutation_probability:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

def genetic_algorithm(population_size, chromosome_size, generations, mutation_probability):
    population = initialize_population(population_size, chromosome_size)

    for generation in range(generations):
        fitness_scores = [fitness_evaluation(chromosome) for chromosome in population]

        new_population = []

        total_fitness = sum(fitness_scores)
        probabilities = [score / total_fitness for score in fitness_scores]

        for _ in range(population_size // 2):
            parent1 = random.choices(population, weights=probabilities)[0]
            parent2 = random.choices(population, weights=probabilities)[0]

            child1, child2 = crossover(parent1, parent2)

            child1 = mutation(child1, mutation_probability)
            child2 = mutation(child2, mutation_probability)

            new_population.extend([child1, child2])

        population = new_population

    best_chromosome = max(population, key=objective_function)
    best_solution = objective_function(best_chromosome)

    return best_chromosome, best_solution

population_size = 200
chromosome_size = 10
generations = 10
mutation_probability = 0.2

best_chromosome, best_solution = genetic_algorithm(
    population_size, chromosome_size, generations, mutation_probability
)

print("Best chromosome:", best_chromosome)
print("Best solution:", best_solution)
