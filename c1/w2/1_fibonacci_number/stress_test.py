import numpy as np
from fibonacci import calc_fib


def calc_fib_slow(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 30, 1)[0]
        slow = calc_fib_slow(n)
        fast = calc_fib(n)
        if slow == fast:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
