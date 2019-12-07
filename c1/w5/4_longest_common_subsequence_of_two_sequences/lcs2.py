# python3
import sys
import numpy as np


def lcs2(s, t):
    sim = np.zeros((len(s) + 1, len(t) + 1), dtype=int)
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                sim[i, j] = sim[i-1, j-1] + 1
            else:
                sim[i, j] = max(sim[i-1, j], sim[i, j-1])

    return np.max(sim)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
