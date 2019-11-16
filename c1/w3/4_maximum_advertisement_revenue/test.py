from dot_product import max_dot_product
import itertools
import numpy as np


def max_dot_product_slow(a, b):
    all_possible = [zip(x, b) for x in itertools.permutations(a, len(b))]
    all_results = np.zeros((len(all_possible)))
    for i, possible in enumerate(all_possible):
        for pos in possible:
            all_results[i] += pos[0] * pos[1]

    return int(np.max(np.max(all_results)))


if __name__ == '__main__':

    while True:
        n = np.random.randint(0, 10, 1)[0]
        a = list(np.random.randint(-1000, 1000, n))
        b = list(np.random.randint(-1000, 1000, n))
        slow = max_dot_product_slow(a, b)
        fast = max_dot_product(a, b)
        if slow == fast:
            print(n, a, b, 'OK')
        else:
            print(n, slow, fast)
            break
