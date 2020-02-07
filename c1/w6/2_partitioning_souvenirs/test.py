import itertools
import numpy as np
from partition3 import partition3
import time


def partition3_slow(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


if __name__ == '__main__':
    while True:
        n = np.random.randint(1, 10, 1)[0]
        objs = list(np.random.randint(1, 30, n))
        print(objs, sum(objs) / 3)
        start = time.time()
        result1 = partition3_slow(objs)
        end = time.time()
        delta1 = end - start
        print(result1)

        start = time.time()
        result2 = partition3(objs)
        end = time.time()
        delta2 = end - start
        if result1 == result2:
            print('OK!', delta1, delta2)
        else:
            print(result2)
            break


