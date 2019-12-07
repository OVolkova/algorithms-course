from edit_distance import edit_distance
import Levenshtein
import numpy as np
CHARS = 'qwertyuiopasdfghjklzxcvbnm'

if __name__ == '__main__':
    while True:
        n = np.random.randint(0, 10, 1)[0]
        m = np.random.randint(0, 10, 1)[0]
        a = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), n)])
        b = ''.join([CHARS[i] for i in np.random.randint(0, len(CHARS), m)])
        lev = Levenshtein.distance(a, b)
        mine = edit_distance(a, b)
        if lev == mine:
            print(a, b, 'OK')
        else:
            print(a, b)
            break
        lev = Levenshtein.distance(a, a)
        mine = edit_distance(a, a)
        if lev == mine:
            print(a, a, 'OK')
        else:
            print(a, a)
            break
