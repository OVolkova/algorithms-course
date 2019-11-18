from inversions import get_number_of_inversions
import numpy as np
import copy


def get_number_of_inversions_naive(a):
    number_of_inversions = 0
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    i = 0
    error = False
    while True:
        n = np.random.randint(1, 20, 1)[0]
        a = list(np.random.randint(1, 100, n))
        #a = [1, 8, 1, 7, 1]
        #n = len(a)
        aa = copy.deepcopy(a)
        slow = get_number_of_inversions_naive(a)
        fast = get_number_of_inversions(a, 0, n)
        if fast == slow:
            print(aa,  'OK')
        else:
            print(aa,  slow, fast)
            break
