# python3
import sys


def count_frequency(a, left, right, x):
    count = 0
    for elem in a[left: right]:
        if elem == x:
            count += 1
    return count


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    k = (-left+right)//2
    subleft = get_majority_element(a, left, k+left)
    subright = get_majority_element(a, k+left, right)
    if subleft == subright:
        return subright

    subleft_frequency = count_frequency(a, left, right, subleft)
    if subleft_frequency > k:
        return subleft

    subright_frequency = count_frequency(a, left, right, subright)
    if subright_frequency > k:
        return subright

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
