from binary_search import binary_search
import numpy as np


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    i = 0
    error = False
    while True:
        n = np.random.randint(1, 100, 1)[0]
        m = np.random.randint(1, 50, 1)[0]
        a = list(set(np.random.randint(1, 100, n)))
        b = list(np.random.randint(1, 100, m))

        for x in b:
            # replace with the call to binary_search when implemented
            #a = [8, 5, 2]
            #x = 2
            slow = linear_search(a, x)
            fast = binary_search(a, x)
            if fast == slow:
                print(a, x,  'OK')
            else:
                print(a, x,  slow, fast)
                error = True
                break
        if error:
            break
