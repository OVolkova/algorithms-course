import os
from  job_queue import  assign_jobs
import time
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])



def assign_jobs_slow(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


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
            data = list(map(int, file.readline().split()))

        with open(os.path.join('./tests', answer), 'r') as file:
            jobs = [tuple([int(i) for i in f.strip().split(' ')]) for f in file.readlines() if f.strip()]

        yield data, n, m, jobs


def main():
    Test = iter_tests()
    i = 0
    iterate = True
    while iterate:
        try:
            data, n, m, jobs = next(Test)
            st = time.time()
            assigned_jobs = assign_jobs(n, data)
            etf = time.time()
            assigned_jobs_ = assign_jobs_slow(n, data)
            ets = time.time()
            print(etf - st, ets-etf)
            jobs_ = []
            for job in assigned_jobs:
                jobs_.append((job.worker, job.started_at))

            assert jobs_ == jobs

            i += 1
        except StopIteration:
            iterate = False


if __name__ == '__main__':
    main()
