from itertools import  combinations
from knapsack import optimal_weight
import numpy as np


def slow(objects, W):
    max_weight = 0
    objects_nums = list(range(0, len(objects)))
    for i in range(0, len(objects)+1):
        objects_combinations = combinations(objects_nums, i)
        for combination in objects_combinations:
            weight = 0
            for num in combination:
                weight += objects[num]
            if max_weight < weight <= W:  # and weight > max_weight:
                max_weight = weight
    return max_weight


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 20, 1)[0]
        W = np.random.randint(0, 1000, 1)[0]
        objs = list(np.random.randint(0, 300, n))
        result1 = slow(objs, W)
        result2 = optimal_weight(objs, W)
        if result1 == result2:
            print(objs, W, result1, 'OK!')
        else:
            print(objs, W, result1, result2)
            break
