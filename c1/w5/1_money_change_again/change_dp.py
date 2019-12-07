# python3


def get_change(m, coins=(1, 3, 4)):
    min_coins = {0: 0}
    for i in range(1, m+1):
        min_coins[i] = float('Inf')
        for c in coins:
            if c <= i:
                num_coins = min_coins[i-c] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
