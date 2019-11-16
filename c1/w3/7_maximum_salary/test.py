from largest_number import largest_number
import numpy as np
import itertools


def largest_number_slow(a):
    alls = []
    for combination in itertools.permutations(a, len(a)):
        alls.append(int(''.join([str(c) for c in combination])))

    return sorted(alls, reverse=True)[0]


if __name__ == '__main__':
    i = 0
    while True:
        n = np.random.randint(1, 3, 4)
        data = []
        for i, j in enumerate(list(n)):
            data += list(np.random.randint(10**i, 10**(i+1), j))
        slow = largest_number_slow(data)
        fast = largest_number(data)
        if fast == slow:
            print(data,  'OK')
        else:
            print(data,  slow, fast)
            break
