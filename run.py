import random
from numpy import r_
import optimize
import roots

def make_random_coord(size):
    return (random.randint(0, size), random.randint(0, size))

## make n random cities
n = 50
map_size = 1000
cities = [make_random_coord(map_size) for i in r_[0:n]]

# find the best route
path = optimize.find_best_route(cities)
print(path)

