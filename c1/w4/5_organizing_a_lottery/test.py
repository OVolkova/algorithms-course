from points_and_segments import fast_count_segments
import numpy as np


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    i = 0
    error = False
    while True:
        n = np.random.randint(1, 10, 1)[0]
        m = np.random.randint(1, 10, 1)[0]
        starts = np.random.randint(-20, 20, n)
        deltas = np.random.randint(0, 20, n)
        ends = starts+deltas
        points = list(np.random.randint(-20, 20, m))
        starts = list(starts)
        ends = list(ends)

        slow = naive_count_segments(starts, ends, points)
        fast = fast_count_segments(starts, ends, points)
        if fast == slow:
            print(starts, ends, points,  'OK')
        else:
            print(starts, ends, points,  slow, fast)
            break
