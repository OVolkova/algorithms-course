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


def fibonacci_sum_squares(n):
    m = 10
    pisano_seq = get_pisano_period(m)
    pisano_seq = [p * p for p in pisano_seq]
    period = len(pisano_seq)
    nums = (n // period) % 10
    last = n % period
    pisano_seq_sum = sum(pisano_seq) % 10
    last_pisano_seq_sum = sum(pisano_seq[:last+1]) % 10

    return (nums * pisano_seq_sum + last_pisano_seq_sum) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
