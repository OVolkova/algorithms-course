import numpy as np
from fibonacci_huge import get_fibonacci_huge


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    while True:
        n = np.random.randint(1, 50, 1)[0]
        m = np.random.randint(2, 100, 1)[0]
        slow = get_fibonacci_huge_naive(n, m)
        fast = get_fibonacci_huge(n, m)
        if slow == fast:
            print(n, m, 'OK')
        else:
            print(n, m, slow, fast)
            break
