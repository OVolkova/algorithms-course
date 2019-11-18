# python3
import sys
import random
random.seed(1)

def partition3(a, l, r):
    x = a[l]
    j = l
    l_fixed = l
    for i in range(l_fixed + 1, r):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            l += 1
            j += 1
            if j != l:
                temp_l = a[l]
                a[l] = a[i]
                a[i] = a[j]
                a[j] = temp_l
            else:
                a[i], a[j] = a[j], a[i]

    delta = l - l_fixed
    for i in range(0, delta+1):
        if l_fixed+i == j-i:
            break
        a[l_fixed+i], a[j-i] = a[j-i], a[l_fixed+i]

    return j-delta, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l + 1 >= r:
        return
    k = random.randint(l, r-1)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m_low, m_up = partition3(a, l, r)
    if l < m_low:
        randomized_quick_sort(a, l, m_low)
    if m_up+1 < r:
        randomized_quick_sort(a, m_up + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n)
    for x in a:
        print(x, end=' ')
