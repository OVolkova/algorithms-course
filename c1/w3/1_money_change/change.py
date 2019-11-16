# python3


def get_change(m):
    coins = [10, 5, 1]
    n = 0
    for coin in sorted(coins, reverse=True):
        n += m // coin
        m = m % coin
        if m == 0:
            break

    return n


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
