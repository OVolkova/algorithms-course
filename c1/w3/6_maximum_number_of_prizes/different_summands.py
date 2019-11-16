# python3
import sys
import numpy as np


def optimal_summands(n):
    m = 1
    while True:
        k = n - m*(m+1)/2
        if k > m:
            m += 1
        else:
            break

    summands = np.ones((m,), dtype=int)
    for i in range(1, m):
        summands[i] += summands[i-1]

    summands[m-1] += k

    return list(summands)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
