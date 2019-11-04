# python3


def lcm(a, b):
    return int(abs(a*b)/gcd(a, b))


def gcd(a, b):
    if b == 0:
        return a
    else:
        reminder = a % b
        return gcd(b, reminder)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

