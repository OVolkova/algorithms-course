from sorting import randomized_quick_sort
import numpy as np
import copy
import random

random.seed(1)


def sort_naive(ar):
    return sorted(ar)


if __name__ == '__main__':
    i = 0
    error = False
    while True:
        n = np.random.randint(1, 100, 1)[0]
        a = list(np.random.randint(1, 100, n))
        a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        n = len(a)
        copied_a = copy.deepcopy(a)
        slow = sort_naive(copy.deepcopy(a))
        randomized_quick_sort(a, 0, n)
        if a == slow:
            print(copied_a,  'OK', slow, a)
        else:
            print(copied_a,  slow, a)
            break
