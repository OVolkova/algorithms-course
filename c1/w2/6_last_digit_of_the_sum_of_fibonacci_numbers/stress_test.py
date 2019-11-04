import numpy as np
from fibonacci_sum_last_digit import fibonacci_sum


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


if __name__ == '__main__':
    while True:
        n = np.random.randint(1, 100, 1)[0]
        slow = fibonacci_sum_naive(n)
        fast = fibonacci_sum(n)
        if slow == fast:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
