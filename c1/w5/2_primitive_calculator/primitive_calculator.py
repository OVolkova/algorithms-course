# python3


def optimal_sequence(n):
    min_operations = {1: 0}
    prevlem = {1: None}
    for i in range(2, n+1):
        min_operations[i] = float('Inf')
        prevlem[i] = None
        if i % 3 == 0:
            num_operations = min_operations[i // 3] + 1
            if num_operations <= min_operations[i]:
                min_operations[i] = num_operations
                prevlem[i] = i // 3
        if i % 2 == 0:
            num_operations = min_operations[i // 2] + 1
            if num_operations <= min_operations[i]:
                min_operations[i] = num_operations
                prevlem[i] = i // 2

        num_operations = min_operations[i - 1] + 1
        if num_operations <= min_operations[i]:
            min_operations[i] = num_operations
            prevlem[i] = i - 1

    sequence = [n]
    elem = prevlem[n]
    while elem:
        sequence.append(elem)
        elem = prevlem[elem]
    sequence.reverse()
    return sequence


if __name__ == '__main__':
    n = int(input())
    osequence = list(optimal_sequence(n))
    print(len(osequence) - 1)
    for x in osequence:
        print(x, end=' ')
