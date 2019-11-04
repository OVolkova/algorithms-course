import numpy as np
from gcd import gcd


def gcd_naive(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 100000, 2)
        a, b = n[0], n[1]
        slow = gcd_naive(a, b)
        fast = gcd(a, b)

        if slow == fast:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
