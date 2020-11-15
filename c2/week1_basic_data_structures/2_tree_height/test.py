import os
from tree_height import TreeHeight

import sys
import threading

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
            parents = list(map(int, file.readline().split()))
            data = (n, parents)

        with open(os.path.join('./tests', answer), 'r') as file:
            a = file.readline()
            result = int(a)

        yield data, result


def main():
    Test = iter_tests()
    i = 0
    iterate = True
    while iterate:
        try:
            data, result = next(Test)
            tree = TreeHeight(data[0], data[1])
            print(i, result, tree.compute_height())

            assert result == tree.compute_height()
            i += 1
        except StopIteration:
            iterate = False


sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()


