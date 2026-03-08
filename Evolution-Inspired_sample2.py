import random

population = [random.randint(-10,10) for _ in range(6)]

def fitness(x):
    return -(x**2) + 10

for generation in range(10):

    new_population = []

    for individual in population:
        mutation = individual + random.randint(-2,2)
        new_population.append(mutation)

    combined = population + new_population
    combined.sort(key=fitness, reverse=True)

    population = combined[:6]

    print("Generation", generation, "Best:", population[0])