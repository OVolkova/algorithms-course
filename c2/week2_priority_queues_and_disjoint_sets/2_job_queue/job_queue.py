# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    pq = [(0, n) for n in range(0, n_workers)]
    heapq.heapify(pq)
    for job in jobs:
        free_time, thread = heapq.heappop(pq)
        result.append(AssignedJob(started_at=free_time, worker=thread))
        heapq.heappush(pq, (free_time+job, thread))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
