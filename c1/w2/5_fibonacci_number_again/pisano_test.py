from fibonacci_huge import get_pisano_period

if __name__ == '__main__':
    for i, n in enumerate([1, 3, 8, 6, 20, 24, 16, 12, 24, 60, 10, 24, 28, 48, 40, 24, 36, 24, 18, 60, 16, 30, 48, 24, 100, 84, 72, 48, 14, 120, 30, 48, 40, 36, 80, 24, 76, 18, 56, 60, 40, 48, 88, 30, 120, 48, 32, 24, 112, 300, 72, 84, 108, 72, 20, 48, 72, 42, 58, 120, 60, 30, 48, 96, 140, 120, 136]):
        period = len(get_pisano_period(i+1))
        if n == period:
            print(i+1, 'OK')
        else:
            print(i+1, n, period)
            break
