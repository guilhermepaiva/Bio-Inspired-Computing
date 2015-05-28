import random
import math
import numpy as np 
import matplotlib.pyplot as plt 

nof_glowworms = 300 # population's size
dimension = 30 # number of parameters of the function [x1, x2, x3, ... , x30]
rho = 0.4 # luciferin decay (0 < rho < 1)
gamma = 0.6 # luciferin enhancement
beta = 0.08 # model constant
nof_neighbors = 5
step_size = 0.03
initial_luciferin = 4
initial_sensor_range = 120.0 # a constant, which limits the size of the neighbourhood range
max_iteration = 1000 # number of iterations (loop)
glowworm_population = []
min_neighbours = math.ceil(nof_glowworms*0.03)
max_neighbours = math.ceil(nof_glowworms*0.2)
array_best_fitness = []


def calculate_ackley(glowworm):
	a, b, c = 20.0, 0.2, (math.pi)*2.0
	first_sum = 0.0
	for i in range(len(glowworm)-1):
		first_sum += glowworm[i]**2.0
	first_sum = math.sqrt(first_sum * (1.0/(len(glowworm)-1)))
	first_sum *= -b
	second_sum = 0.0
	for j in range(len(glowworm)-1):
		second_sum += math.cos(c*glowworm[j])
	second_sum *= (1.0/(len(glowworm)-1))
	result = (-a * math.exp(first_sum)) - math.exp(second_sum) + a + math.exp(1)
	return result

def calculate_fitness(glowworm):
	return 1.0/(calculate_ackley(glowworm) + 1.0)

def create_glowworm():
	return {'params':[random.uniform(-15.0,15.0) for x in range(dimension)], 'luciferin':initial_luciferin, 'sensor_range':initial_sensor_range}

def deploy_agents():
	population = []
	for i in range(0, nof_glowworms):
		population.append(create_glowworm())
	return population

def update_luciferin(glowworm):
	J = calculate_fitness(glowworm['params'])
	li = glowworm['luciferin']
	return (((1-rho) * li) + (gamma*J))

def get_neighbours(glowworm_i, population):
	neighbours = []
	for glowworm_j in population:
		dij = calculate_distance(glowworm_j, glowworm_i)
		if ((dij < glowworm_i['sensor_range']) and (dij != 0) and (glowworm_i['luciferin'] < glowworm_j['luciferin'])):
			neighbours.append(glowworm_j)
	return neighbours


def calculate_distance(glowworm1, glowworm2):
	a = np.array(glowworm1['params'])
	b = np.array(glowworm2['params'])
	distance = np.linalg.norm(a-b)
	return distance

def calculate_probability(glowworm_i, glowworm_j, neighbours):
	return ((glowworm_j['luciferin'] - glowworm_i['luciferin']) / (sum_difference_luciferin(glowworm_i, neighbours)))


def sum_difference_luciferin(glowworm_i, neighbours):
	result = 0.0
	for each_neighbour in neighbours:
		result += each_neighbour['luciferin'] - glowworm_i['luciferin']
	return result

def select_glowworm(probability_array):
	wheel = []
	for i in range(len(probability_array)):
		if (i == 0):
			wheel.append(probability_array[i])
		else:
			wheel.append(probability_array[i] + wheel[i-1])
	random_position = random.random()
	for index in range(len(wheel)):
		if (random_position <= wheel[index]):
			return index
	return 0

def new_sensor_range(glowworm, neighbours_amount):
	new_range = glowworm['sensor_range'] + beta*(nof_neighbors - neighbours_amount)
	new_range = max(0,new_range)
	return min(initial_sensor_range,new_range)

def new_position(glowworm_i, glowworm_j):
	vector = [x - y for x, y in zip(glowworm_j['params'], glowworm_i['params'])]
	norm = np.linalg.norm(vector)
	result = np.divide(vector, norm)
	result += step_size
	result = np.add(result, glowworm_i['params'])
	return result.tolist()



#print create_glowworm()['luciferin'] mostra somente a luciferina
glowworm_population = deploy_agents()

t = 0
while (t <= max_iteration):

	# Luciferin update phase
	for each_glowworm in glowworm_population:
		each_glowworm['luciferin'] = update_luciferin(each_glowworm)

	# movement phase
	for each_glowworm_i in glowworm_population:
		neighbours = get_neighbours(each_glowworm_i, glowworm_population)
		if (min_neighbours <= len(neighbours) <= max_neighbours):
			p = []
			for each_neighbour_j in neighbours:
				p.append(calculate_probability(each_glowworm_i, each_neighbour_j, neighbours))
			j = neighbours[select_glowworm(p)]
			each_glowworm_i['params'] = new_position(each_glowworm_i, j)
		#atualiza o raio
		#automaticamente, se o numero de vizinhos for baixo o range aumenta, e o inverso tambem eh verdade
		each_glowworm_i['sensor_range'] = new_sensor_range(each_glowworm_i,len(neighbours))

	population_sorted = sorted(glowworm_population, key=lambda x:calculate_fitness(x['params']))

	array_best_fitness.append(calculate_fitness(population_sorted[-1]['params']))

	t += 1

plt.plot(range(0, max_iteration+1), array_best_fitness)
plt.show()


