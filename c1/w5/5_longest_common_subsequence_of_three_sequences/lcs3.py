# python3
import numpy as np
import sys


def lcs3(a, b, c):
    sim = np.zeros((len(a) + 1, len(b) + 1,  len(c) + 1), dtype=int)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    sim[i, j, k] = sim[i-1, j-1, k-1] + 1
                else:
                    sim[i, j, k] = max(sim[i-1, j, k], sim[i, j-1, k], sim[i, j, k-1],
                                       sim[i, j-1, k-1], sim[i-1, j, k-1], sim[i-1, j-1, k])

    return np.max(sim)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
