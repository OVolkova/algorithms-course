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


def fibonacci_sum(n, pisano_seq):
    period = len(pisano_seq)
    nums = (n // period) % 10
    last = n % period
    pisano_seq_sum = sum(pisano_seq) % 10
    last_pisano_seq_sum = sum(pisano_seq[:last+1]) % 10

    return (nums * pisano_seq_sum + last_pisano_seq_sum) % 10


def fibonacci_partial_sum(from_, to):
    m = 10
    pisano_seq = get_pisano_period(m)
    sum_from = fibonacci_sum(from_-1, pisano_seq)
    sum_to = fibonacci_sum(to, pisano_seq)
    if sum_from > sum_to:
        sum_to += 10

    return (sum_to - sum_from) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
