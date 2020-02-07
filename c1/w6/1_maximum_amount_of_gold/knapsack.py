# Uses python3
import sys
import numpy as np


def optimal_weight(objects, W):
    values = np.zeros((W+1, len(objects)+1), dtype=int)
    for i in range(1, len(objects)+1):
        i_weight = objects[i-1]
        for w in range(1, W+1):
            values[w, i] = values[w, i-1]
            if i_weight <= w:
                value = values[w-i_weight, i-1] + i_weight
                if values[w, i] < value:
                    values[w, i] = value

    return np.max(values)


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(w, W))
