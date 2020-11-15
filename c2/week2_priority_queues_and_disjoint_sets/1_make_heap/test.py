import os
from build_heap import Heap


def iter_tests():
    tests = {}
    for name in sorted(os.listdir('./tests')):
        if name.split('.'):
            tests[name.split('.')[0]] = name
        else:
            tests[name] = None

    for test, answer in tests.items():
        print(test)
        with open(os.path.join('./tests', test), 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().split()))

        with open(os.path.join('./tests', answer), 'r') as file:
            m = int(file.readline())
            swaps = []
            for i in range(0, m):
                swaps.append(tuple([int(i) for i in file.readline().strip().split(' ')]))

        yield data, n, swaps, m


def main():
    Test = iter_tests()
    i = 0
    iterate = True
    while iterate:
        try:
            data, n, swaps, m = next(Test)

            heap = Heap(data, n)
            heap.build_heap()
            print(i, n, m, heap.swaps_counter, 4*n)

            assert heap.swaps_counter == m
            assert heap.swaps == swaps
            i += 1
        except StopIteration:
            iterate = False


if __name__ == '__main__':
    main()
