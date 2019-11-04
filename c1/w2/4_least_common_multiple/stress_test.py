import numpy as np
from lcm import lcm


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 1000, 2)
        a, b = n[0], n[1]
        slow = lcm_naive(a, b)
        fast = lcm(a, b)

        if slow == fast:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
