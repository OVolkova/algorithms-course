from lcs2 import lcs2
import numpy as np
#CHARS = 'qwertyuiopasdfghjklzxcvbnm'
CHARS = 'xcvbnm'


# solution from internet
def lcs2_slow(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs2_slow(X, Y, m - 1, n - 1)
    else:
        return max(lcs2_slow(X, Y, m, n - 1), lcs2_slow(X, Y, m - 1, n))


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 10, 1)[0]
        m = np.random.randint(0, 10, 1)[0]
        a = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), n)])
        b = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), m)])
        lev = lcs2_slow(a, b, n, m)
        mine = lcs2(a, b)
        if lev == mine:
            print(a, b, 'OK', lev)
        else:
            print(a, b, lev, mine)
            break
