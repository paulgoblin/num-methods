import random
from numpy import r_
from anneal import find_best_route

def make_random_coord(size):
    return (random.randint(0, size), random.randint(0, size))

## make n random cities
n = 50
map_size = 1000
cities = [make_random_coord(map_size) for i in r_[0:n]]

# find the best route
initial_temp = 50
num_iter = 10000
print_progress = True
path = find_best_route(cities, initial_temp, num_iter, print_progress)
print(path)

