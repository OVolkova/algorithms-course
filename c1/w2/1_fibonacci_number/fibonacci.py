# python3


def calc_fib(n):
    if n <= 1:
        return n
    f_2 = 0
    f_1 = 1
    for i in range(1, n):
        f_2, f_1 = f_1, f_1 + f_2

    return f_1


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
