import random

def initialize_population(n=10, m=10):
    return [[random.randint(0, 1) for _ in range(m)] for _ in range(n)] # initialize n individuals with m genes

def fitness(individual):
    return sum(individual) # sum of all genes, highest fitness is the biggest sum

def sort_population(population):
    # returns a tuple of (fitness, individual) sorted by fitness in descending order
    return sorted([(fitness(individual), individual) for individual in population], key=lambda x: x[0], reverse=True)

def selection(sorted_population, percentage=0.5):
    #use roulette wheel selection to select percentage of the population
    n = len(sorted_population)
    fitnesses = [fitness for fitness, _ in sorted_population]
    total_fitness = sum(fitnesses)
    selected = []
    while len(selected) < n * percentage:
        r = random.uniform(0, total_fitness)
        for i, fitness in enumerate(fitnesses):
            r -= fitness
            if r <= 0:
                selected.append(sorted_population[i][1])
                break
    return selected




def crossover(individual1, individual2):
    n = len(individual1)
    return individual1[:n//2] + individual2[n//2:]

def crossover_population(selected_population, target_population_size=10):
    # crossover each individual with the next one 2 times to get 2 children
    # add the children to the population
    population = []
    for i in range(0, len(selected_population) -1, 2):
        for _ in range(2):
            population.append(crossover(selected_population[i], selected_population[i+1]))
            population.append(crossover(selected_population[i+1], selected_population[i]))
    return population[:target_population_size]

def mutation(individual, probability=0.1):
    for i in range(len(individual)):
        if random.random() < probability:
            individual[i] = 1 - individual[i]
    return individual

def mutate_population(population, probability=0.1):
    return [mutation(individual, probability) for individual in population]

def run_genetic_algorithm(max_iter_count=100, population_size=10, gene_size=10, desired_fitness=10):
    population = initialize_population(population_size, gene_size)
    print("Initial Population: ")
    print('\n'.join([' '.join(map(str, individual)) for individual in population]))
    print("-----------------")
    for _ in range(max_iter_count):
        sorted_population = sort_population(population)
        if sorted_population[0][0] >= desired_fitness:
            return sorted_population[0]
        print("Sorted Population: ")
        print('\n'.join([' '.join(map(str, (fitness, individual))) for fitness, individual in sorted_population]))
        print("-----------------")
        selected_population = selection(sorted_population)
        print("Selected Population: ")
        print('\n'.join([' '.join(map(str, individual)) for individual in selected_population]))
        print("-----------------")
        crossovered_population = crossover_population(selected_population)
        print("Crossovered Population: ")
        print('\n'.join([' '.join(map(str, individual)) for individual in crossovered_population]))
        print("-----------------")
        mutated_population = mutate_population(crossovered_population)
        print("Mutated Population: ")
        print('\n'.join([' '.join(map(str, individual)) for individual in mutated_population]))
        print("-----------------")
    return max(mutated_population, key=lambda x: x[0])


def main():
    print(run_genetic_algorithm())


if __name__ == '__main__':
    main()