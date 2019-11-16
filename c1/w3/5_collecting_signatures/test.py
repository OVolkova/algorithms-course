from covering_segments import optimal_points
import itertools
import numpy as np
from collections import namedtuple
from collections import defaultdict

Segment = namedtuple('Segment', 'start end')


def point_with_items_slow(segments):
    points = set()
    for i, s in segments:
        points.add(s.start)
        points.add(s.end)

    points_with_items = defaultdict(list)
    for point in points:
        for i, s in segments:
            if point >=s.start and point <=s.end:
                points_with_items[point].append(i)

    return points_with_items


def optimal_points_slow(segments):
    segments_ids = range(0, len(segments))
    all_points = point_with_items_slow(list(zip(segments_ids, segments)))
    all_possible_points = []
    for k in range(1, len(all_points.keys())+1):
        for combination in itertools.combinations(all_points.keys(), k):
            items_combination = set()
            for c in combination:
                items_combination = items_combination.union(set(all_points[c]))
            if len(set(segments_ids).difference(items_combination)) == 0:
                all_possible_points.append((list(combination), len(combination)))

    all_possible_points = sorted(all_possible_points, key=lambda x: x[1])
    best_possible_points = []
    best_len = all_possible_points[0][1]
    for possible in all_possible_points:
        if possible[1] == best_len:
            best_possible_points.append(sorted(possible[0], reverse=True))

    return best_possible_points


if __name__ == '__main__':

    while True:
        n = np.random.randint(1, 10, 1)[0]
        segments = [None]*n
        for ni in range(0, n):
            segment = sorted(list(np.random.randint(0, 100, 2)))
            segments[ni] = Segment(segment[0], segment[1])
        #segments = [Segment(start=1, end=3), Segment(start=4, end=6), Segment(start=6, end=9), Segment(start=3, end=5)]
        slow = optimal_points_slow(segments)
        fast = sorted(optimal_points(segments), reverse=True)
        if fast in slow:
            print(n, segments, 'OK')
        else:
            print(n, segments, slow, fast)
            break
