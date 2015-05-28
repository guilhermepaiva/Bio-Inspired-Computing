

nof_glowworms = 30 # population's size
dimension = 30 # number of parameters of the function [x1, x2, x3, ... , x30]
rho = 0.4 # luciferin decay (0 < rho < 1)
gamma = 0.6 # luciferin enhancement
beta = 0.08 # model constant
nof_neighbors = 5
step_size = 0.03
initial_luciferin = 4
initial_sensor_range = # a constant, which limits the size of the neighbourhood range


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

