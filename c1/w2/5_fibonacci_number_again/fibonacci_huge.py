# python3


def get_pisano_period(m):
    if m == 1:
        return [0]
    pisano_seq = [0, 1]
    previous = 0
    current = 1
    while True:
        previous, current = current, previous + current
        pisano_seq.append(current % m)
        if pisano_seq[-2:] == [0, 1]:
            break

    return pisano_seq[:-2]


def get_fibonacci_huge(n, m):
    pisano_seq = get_pisano_period(m)
    period = len(pisano_seq)

    return pisano_seq[n % period]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
