import numpy as np
from max_pairwise_product import max_pairwise_product


def max_pairwise_product_slow(n, array):
    array = sorted(array[:n], reverse=True)
    return array[0]*array[1]


if __name__ == '__main__':

    while True:
        n = np.random.randint(2, 2*100, 1)[0]
        print(n)
        input_array = np.random.randint(0, 100000, n)
        slow = max_pairwise_product_slow(n, input_array)
        fast = max_pairwise_product(n, input_array)
        if slow != fast:
            print('{} <- Fast answer {} <- Slow Answer {}' .format(' '.join([str(a) for a in input_array]), slow, fast))
            break
        else:
            print('{} <- OK '.format(' '.join([str(a) for a in input_array])))
