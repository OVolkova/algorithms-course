# python3
import sys


def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave, right)

    left_i = left
    right_i = ave
    temp = [None]*(right-left)
    k = 0
    while k < (right-left):
        if right_i != right and left_i != ave and a[left_i] > a[right_i]:
            number_of_inversions += ave - left_i #+ 1
            temp[k] = a[right_i]
            k += 1
            right_i += 1
        elif left_i == ave:
            temp[k] = a[right_i]
            k += 1
            right_i += 1
        else:
            temp[k] = a[left_i]
            k += 1
            left_i += 1

    for i in range(left, right):
        a[i] = temp[i-left]

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #b = n * [0]
    print(get_number_of_inversions(a, 0, len(a)))
