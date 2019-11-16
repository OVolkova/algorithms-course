from different_summands import optimal_summands
import numpy as np


def optimal_summands_slow(n):
    k = 0
    summands = []
    while n > k:
        k += 1
        summands.append(k)
        n -= k
    summands[-1] += n

    return summands


if __name__ == '__main__':

    while True:
        n = np.random.randint(1, 10000000000, 1)[0]
        slow = optimal_summands_slow(n)
        fast = optimal_summands(n)
        if fast == slow:
            print(n, 'OK')
        else:
            print(n, slow, fast)
            break
