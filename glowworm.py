import random
import math
import numpy as np 

nof_glowworms = 30 # population's size
dimension = 30 # number of parameters of the function [x1, x2, x3, ... , x30]
rho = 0.4 # luciferin decay (0 < rho < 1)
gamma = 0.6 # luciferin enhancement
beta = 0.08 # model constant
nof_neighbors = 5
step_size = 0.03
initial_luciferin = 4
initial_sensor_range = 3 # a constant, which limits the size of the neighbourhood range
max_iteration = 100 # number of iterations (loop)


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
	for glowworm_j in population:
		dij = calculate_distance(glowworm_j, glowworm_i)
		if (dij < glowworm_i['sensor_range'])

def calculate_distance(glowworm1, glowworm2):
	a = np.array(glowworm1['params'])
	b = np.array(glowworm2['params'])
	distance = np.linalg.norm(a-b)
	return distance


#print create_glowworm()['luciferin'] mostra somente a luciferina
gw1 = create_glowworm()
gw2 = create_glowworm()
print gw1
print "*"*90
print gw2
print "*"*90
print "Distance: "
print calculate_distance(gw1, gw2)




