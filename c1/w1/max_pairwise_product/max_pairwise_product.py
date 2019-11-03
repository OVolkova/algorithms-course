# python3


def max_pairwise_product(n, array):
    max_elems = sorted(array[:2])
    for i in array[2: n]:
        if i > max_elems[0]:
            if i > max_elems[1]:
                max_elems[0] = max_elems[1]
                max_elems[1] = i
            else:
                max_elems[0] = i

    return max_elems[0] * max_elems[1]


if __name__ == '__main__':
    n = int(input())
    input_array = [int(i) for i in input().split()]
    print(max_pairwise_product(n, input_array))
