import os
from merging_tables import Database
import time


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
            n, m = tuple([int(i) for i in file.readline().strip().split(' ')])
            sizes = list(map(int, file.readline().split()))
            assert len(sizes) == n
            to_merge = [(None, None)]*m
            for iteration in range(0, m):
                to_merge[iteration] = tuple([int(k) for k in file.readline().strip().split(' ')])

        with open(os.path.join('./tests', answer), 'r') as file:
            answers = [int(f) for f in file.readlines() if f.strip()]

        yield n, m, sizes, to_merge, answers


def main():
    Test = iter_tests()
    i = 0
    iterate = True
    while iterate:
        try:
            n, m, sizes, to_merge, answers = next(Test)
            st = time.time()
            db = Database(sizes)
            maxs = []
            for src, dst in to_merge:
                db.merge(src-1, dst-1)
                maxs.append(db.max_row_count)
            etf = time.time()
            print(etf - st)

            assert maxs == answers
            i += 1

        except StopIteration:
            iterate = False


if __name__ == '__main__':
    main()
