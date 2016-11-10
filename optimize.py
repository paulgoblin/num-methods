import math
import random
from numpy import r_, subtract, copy

def _compute_tour_distance(order, cities):
    tour = [cities[i] for i in order]
    dist = 0
    prev_city = tour[0]
    for city in tour:
        diff = subtract(prev_city, city)
        dist += math.sqrt(sum([d**2 for d in diff]))
        prev_city = city

    return dist

def _compute_acceptance_probablity(old, new, T):
    if (new < old):
        return 1
    return math.exp((old - new)/T)

def find_best_route(cities):
    best_so_far = float('inf')
    worst_so_far = -1*float('inf')
    count = 0

    n = len(cities)
    initialTemp = 50
    numIter = 10000

    order = r_[0:n]
    dist = _compute_tour_distance(order, cities)

    for T in r_[initialTemp:1:numIter*1j]:
        # get neighboring solution
        new_order = copy(order)
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        new_order[i], new_order[j] = new_order[j], new_order[i]
        new_dist = _compute_tour_distance(new_order, cities)

        # decide whether to accept neighbor
        P_accept = _compute_acceptance_probablity(dist, new_dist, T)
        should_accept = random.random() < P_accept
        if should_accept:
            order = new_order
            dist = new_dist

        # save diagnostics
        if (new_dist < best_so_far):
            best_so_far = new_dist
        if (new_dist > worst_so_far):
            worst_so_far = new_dist

        # report progress
        count += 1
        if count%100 == 0:
            print('T:', round(T), 'dist:', round(dist))

    print('Best route dist', round(best_so_far))
    print('Worst route dist', round(worst_so_far))
    return (order.tolist(), dist)





