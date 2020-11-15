import numpy as np
from max_sliding_window import max_sliding_window
import time


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


if __name__ == '__main__':
    while True:
        n = np.random.randint(10, 11, 1)[0]
        if n == 1:
            window_size = 1
        else:
            window_size = np.random.randint(3, 4, 1)[0]

        input_array = np.random.randint(0, 100000, n)

        st = time.time()
        naive = max_sliding_window_naive(input_array, window_size)
        etn = time.time()
        fast = max_sliding_window(input_array, window_size)
        etf = time.time()

        if naive != fast:
            print(input_array, window_size, naive, fast)
        else:
            print(len(input_array), window_size, etn-st, etf-etn)
        assert naive == fast

