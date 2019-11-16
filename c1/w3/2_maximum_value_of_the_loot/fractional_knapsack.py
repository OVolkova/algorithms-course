# python3
import numpy as np


def get_optimal_value(capacity, weights, values):
    values_per_weight = values / weights
    items = sorted(zip(list(values_per_weight), list(values), list(weights)),
                   reverse=True, key=lambda x: (x[0], x[1], x[2]))
    total_value = 0.
    for value_per_weight, value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value_per_weight*capacity
            break

    return round(total_value, 4)


if __name__ == "__main__":
    n, capacity = list(map(int, input().split()))
    values = np.zeros((n,))
    weights = np.zeros((n,))
    for ni in range(0, n):
        values[ni], weights[ni] = list(map(int, input().split()))
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
