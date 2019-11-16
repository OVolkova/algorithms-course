from fractional_knapsack import get_optimal_value
import numpy as np
import itertools


def get_optimal_value_slow(capacity, weights, values):
    a = list(range(0, len(weights)))
    alls = []
    for combination in itertools.permutations(a, len(a)):
        value = 0
        c_capacity = capacity
        for c in combination:
            if c_capacity >= weights[c]:
                value += values[c]
                c_capacity -= weights[c]
            else:
                value += values[c] / weights[c] * c_capacity
                break
        alls.append(value)

    return round(sorted(alls, reverse=True)[0], 4)


if __name__ == '__main__':

    tests = [(66, np.array([44, 99]), np.array([60, 64])),
             (50, np.array([60, 100, 120]), np.array([20, 50, 30]), 180.),
             (10, np.array([500]), np.array([30]), 166.6667),
             (10, np.array([20, 10, 20]), np.array([20, 5, 4]), 31.)]

    for test in tests:
        c, w, v = test[0], test[2], test[1]
        fast = get_optimal_value(c, w, v)
        slow = get_optimal_value_slow(c, w, v)
        if (fast - slow) <= 10 ** (-3):
            print(c, w, v, 'OK')
        else:
            print(c, w, v, slow, fast)
            break

    while True:
        n = np.random.randint(1, 5, 1)[0]
        c = np.random.randint(1, 100, 1)[0]
        w = np.random.randint(1, 100, n)
        v = np.random.randint(1, 100, n)
        fast = get_optimal_value(c, w, v)
        slow = get_optimal_value_slow(c, w, v)
        if (fast - slow) <= 10**(-3):
            print(c, w, v,  'OK')
        else:
            print(c, w, v,  slow, fast)
            break