from lcs3 import lcs3
import numpy as np
#CHARS = 'qwertyuiopasdfghjklzxcvbnm'
CHARS = 'xcvbnm'


# solution from internet
def lcsOf3(X, Y, Z, m, n, o):
    L = [[[0 for i in range(o + 1)] for j in range(n + 1)]
         for k in range(m + 1)]
    ''' Following steps build L[m+1][n+1][o+1] in 
    bottom up fashion. Note that L[i][j][k] 
    contains length of LCS of X[0..i-1] and 
    Y[0..j-1] and Z[0.....k-1] '''
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0

                elif (X[i - 1] == Y[j - 1] and
                      X[i - 1] == Z[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1

                else:
                    L[i][j][k] = max(max(L[i - 1][j][k],
                                         L[i][j - 1][k]),
                                     L[i][j][k - 1])


    return L[m][n][o]


if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 10, 1)[0]
        m = np.random.randint(0, 10, 1)[0]
        p = np.random.randint(0, 10, 1)[0]
        a = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), n)])
        b = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), m)])
        c = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), p)])
        other = lcsOf3(a, b, c, n, m, p)
        mine = lcs3(a, b, c)
        if other == mine:
            print(a, b, c, 'OK', other)
        else:
            print(a, b, c, other, mine)
            break