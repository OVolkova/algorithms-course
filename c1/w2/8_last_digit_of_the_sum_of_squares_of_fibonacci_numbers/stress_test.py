import numpy as np
from fibonacci_sum_squares import fibonacci_sum_squares


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


if __name__ == '__main__':
    while True:
        n = np.random.randint(1, 200, 1)[0]
        slow = fibonacci_sum_squares_naive(n)
        fast = fibonacci_sum_squares(n)
        if slow == fast:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
