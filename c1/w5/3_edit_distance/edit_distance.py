# python3
import numpy as np


def edit_distance(s, t):
    edit = np.zeros((len(s)+1, len(t)+1), dtype=int)
    edit[:, 0] = np.arange(0, len(s)+1, 1, dtype=int)
    edit[0, :] = np.arange(0, len(t)+1, 1, dtype=int)
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            down = edit[i, j-1] + 1
            side = edit[i-1, j] + 1
            diagonal = edit[i-1, j-1]
            if s[i-1] == t[j-1]:
                edit[i, j] = min(down, side, diagonal)
            else:
                edit[i, j] = min(down, side, diagonal+1)

    return edit[len(s), len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
