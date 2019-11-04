import numpy as np
from fibonacci_partial_sum import fibonacci_partial_sum


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    while True:
        nm = sorted(np.random.randint(0, 60, 2))
        n, m = nm[0], nm[1]
        slow = fibonacci_partial_sum_naive(n, m)
        fast = fibonacci_partial_sum(n, m)
        if slow == fast:
            print(n, m, 'OK')
        else:
            print(n, m, slow, fast)
            break
