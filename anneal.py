import math
import random
from numpy import r_, subtract, copy


def find_best_route(cities, initial_temp=50, num_iter=10000, print_progress=False):
    progress_tracker = ProgressTracker(print_progress)
    route = r_[0:len(cities)]
    dist = _compute_route_distance(route, cities)

    for T in r_[initial_temp:1:num_iter*1j]:
        # find neighboring solution
        new_route, new_dist = _get_neighboring_route(route, cities)

        # pick next solution
        route, dist = _choose_next_route(route, dist, new_route, new_dist, T)

        # track solutions
        progress_tracker.track_step(dist, T)

    progress_tracker.done()
    return (route.tolist(), dist)


def _get_neighboring_route(old_route, cities):

    # choose two random cities and swap
    n = len(cities)
    new_route = copy(old_route)
    i, j = random.randint(0, n-1), random.randint(0, n-1)
    new_route[i], new_route[j] = new_route[j], new_route[i]

    # calculate route distance
    new_dist = _compute_route_distance(new_route, cities)

    return new_route, new_dist


def _choose_next_route(route_1, dist_1, route_2, dist_2, T):

    # choose a worse route with some probability P_accept
    P_accept = _compute_acceptance_probablity(dist_1, dist_2, T)
    should_accept = random.random() < P_accept
    if should_accept:
        return route_2, dist_2
    else:
        return route_1, dist_1


def _compute_route_distance(route, cities):

    # compute euclidean distance
    tour = [cities[i] for i in route]
    dist = 0
    prev_city = tour[0]
    for city in tour:
        diff = subtract(prev_city, city)
        dist += math.sqrt(sum([d**2 for d in diff]))
        prev_city = city

    return dist


def _compute_acceptance_probablity(old_dist, new_dist, T):

    # if new_dist is worse, accept it it with some probability determined by T
    if (new_dist > old_dist):
        return math.exp((old_dist - new_dist)/T)
    else: 
        return 1


class ProgressTracker(object):

    def __init__(self, print_progress=False):
        self.print_progress = print_progress
        self.shortest_route_dist = float('inf')
        self.longest_route_dist = -1*float('inf')
        self.count = 0

    def track_step(self, dist, T):
        self.count += 1

        # track best and worst solutions
        if (dist < self.shortest_route_dist):
            self.shortest_route_dist = dist
        if (dist > self.longest_route_dist):
            self.longest_route_dist = dist

        # print progress every 100 steps
        if self.print_progress and (self.count % 100) == 0:
            print('T:', round(T), 'dist:', round(dist))

    def done(self):
        if self.print_progress:
           print('Shortest route', round(self.shortest_route_dist))
           print('Longest route', round(self.longest_route_dist)) 






