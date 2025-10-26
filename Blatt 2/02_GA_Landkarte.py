import random
import matplotlib.pyplot as plt



class Individual:
    def __init__(self, problem):
        self.problem = problem
        self.fitness = 0



def encode_data(data, chunk_size):
    problem = ""
    for i in data:
        bin_chunk = str(bin(i)[2:])
        while len(bin_chunk) < chunk_size:
            bin_chunk = "0" + bin_chunk
        problem += bin_chunk

    return problem


def decode_data(problem, chunk_size):
    return [int(problem[i:i+chunk_size], 2) for i in range(0, len(problem), chunk_size)] # decode problem from bitstring to integer array


def fitness_landkarte(individual):
    data = decode_data(individual.problem, 3)
    fitness = 0

    if data[0] != data[1]: # Color of A != Color of B
        fitness += 5
    if data[1] != data[2]: # B != C
        fitness += 5
    if data[2] != data[3]: # C != D
        fitness += 5
    if data[3] != data[4]: # D != E
        fitness += 5
    if data[0] != data[2]: # A != C
        fitness += 5
    if data[1] != data[3]: # B != D
        fitness += 5

    return fitness - len(list(set(data))) # subtract the numbers of colors in the array from fitness, to get the solution requiring the least colors


def tournament_selection(population, tournament_size):
    mating_pool = []
    while len(mating_pool) < len(population) / 2:
        best = None
        for i in range(0, tournament_size):
            pick = random.choice(population)
            if best is not None:
                if pick.fitness >= best.fitness:
                    best = pick
            else:
                best = pick
        mating_pool.append(best)

    return mating_pool


def crossover(mating_pool, pcross, include_mutation):
    children = []
    while len(children) < len(mating_pool):
        a = random.choice(mating_pool)
        b = random.choice(mating_pool)
        if random.random() < pcross:
            cut_index = random.randint(0, len(a.problem)-1)
            child_a = Individual(a.problem[:cut_index] + b.problem[cut_index:])
            child_b = Individual(a.problem[cut_index:] + b.problem[:cut_index])
            children.append(child_a)
            children.append(child_b)
        else:
            children.append(a)
            children.append(b)

    if include_mutation:
        children = mutate(children, 1/18)

    children.extend(mating_pool)
    return children


def mutate(population, pmut):
    for i in population:
        data = list(i.problem)
        for j in range(0, len(data)):
            if random.random() < pmut:
                if int(data[j]) == 0:
                    data[j] = "1"
                else:
                    data[j] = "0"
        i.problem = "".join(data)
    return population


def evaluate_population(population):
    for i in population:
        i.fitness = fitness_landkarte(i)
    best = max(population, key=lambda x: x.fitness)
    average = sum(x.fitness for x in population) / len(population)
    worst = min(population, key=lambda x: x.fitness)
    return best, average, worst


def genetic_algorith(population_size, max_generations, fitness_cap, tournament_size, pcross, include_mutation=False, verbose=False):
    population = []
    generation = 1

    data_generation = []
    data_best = []
    data_average = []
    data_worst = []

    while len(population) < population_size:
        population.append(Individual(
            encode_data([random.randint(0, 7),
             random.randint(0, 7),
             random.randint(0, 7),
             random.randint(0, 7),
             random.randint(0, 7),
             random.randint(0, 7)], 3)
        ))

    while generation <= max_generations:
        b, a, w = evaluate_population(population)
        if verbose:
            print(f"Generation {generation}: best: {b.fitness}, average: {a}, worst: {w.fitness}")
            data_generation.append(generation)
            data_best.append(b.fitness)
            data_average.append(a)
            data_worst.append(w.fitness)

        if b.fitness >= fitness_cap:
            print(f"Finished after {generation} generations:")
            solutions = []
            for i in population:
                if i.fitness == b:
                    solutions.append(decode_data(i.problem, 3))
                    print(decode_data(i.problem, 3))
            if len(solutions) == 0:
                print(decode_data(b.problem, 3))

            if verbose:
                plt.plot(data_generation, data_best, label="best")
                plt.plot(data_generation, data_average, label="average")
                plt.plot(data_generation, data_worst, label="worst")
                plt.legend(loc="lower right")

                plt.show()

            return generation, True

        mating_pool = tournament_selection(population, tournament_size)
        population = crossover(mating_pool, pcross, include_mutation)
        generation += 1
    return generation, False



def evaluate_algorithm(n):
    data_generation = []
    data_finished = []
    counter_finished = 0

    while n > 0:
        generation, finished = genetic_algorith(10, 500, 27, 5, 0.8, include_mutation=True)
        if finished:
            counter_finished += 1
        data_generation.append(generation)
        data_finished.append(finished)
        n -= 1

    finished_generations = []
    for i in range(0, len(data_generation)):
        if data_finished[i]:
            finished_generations.append(data_generation[i])

    try:
        aes = sum(finished_generations) / len(finished_generations)
    except ZeroDivisionError:
        aes = 'inf'
    sr = len(finished_generations) / len(data_generation)

    print(f"AES: {aes}, SR: {sr}")



evaluate_algorithm(5000)
# genetic_algorith(10, 1000, 27, 5,  0.8, verbose=True, include_mutation=False)