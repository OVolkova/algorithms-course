# python3
import sys


def binary_search(a, x):
    #ar = list(enumerate(a))
    #ar = sorted(ar, key=lambda ax: ax[1])
    start = 0
    end = len(a)
    while end-start > 0:
        middle = (end-start)//2 + start
        if a[middle] == x:
            return middle #ar[middle][0]
        elif a[middle] < x:
            start = middle+1
        else:
            end = middle

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
