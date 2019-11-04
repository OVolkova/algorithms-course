import numpy as np
from fibonacci_last_digit import get_fibonacci_last_digit


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 1000, 1)[0]
        slow = get_fibonacci_last_digit_naive(n)
        fast = get_fibonacci_last_digit(n)
        if slow == fast:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
