from majority_element import get_majority_element
from collections import Counter
import numpy as np
import random


def get_majority_element_naive(a):
    count = Counter(a)
    count = sorted(count.items(), reverse=True, key=lambda x: x[1])
    if count:
        if count[0][1] > len(a)/2:
            return count[0][0]
    return -1


if __name__ == '__main__':
    i = 0
    error = False
    while True:
        n = np.random.randint(1, 200, 1)[0]
        npp = list(np.random.binomial(size=n, n=1, p=0.1))
        nv = np.random.randint(0, 200, n)
        a = []
        for ni, niv in zip(npp, nv):
            if not ni:
                num = np.random.randint(1, 5, 1)[0]
            else:
                num = np.random.randint(90, 100, 1)[0]
            a += [niv]*num
        random.shuffle(a)
        nn = len(a)
        slow = get_majority_element_naive(a)
        fast = get_majority_element(a, 0, nn)
        if fast == slow:
            print(  'OK', slow)
        else:
            print(  slow, fast)
            break
