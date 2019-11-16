# python3
import sys
from collections import namedtuple
from collections import defaultdict
Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments_ids = range(0, len(segments))

    all_points = defaultdict(list)
    for i, s in zip(segments_ids, segments):
        all_points[s.start].append(i)
        all_points[s.end].append(i)

    all_points_sorted = sorted(all_points.keys())
    prev_set = set()
    all_closed_items = set()
    for point in all_points_sorted:
        cur_set = set()
        close_items = set()
        for item in sorted(all_points[point]):
            if item in cur_set:
                close_items.add(item)
            else:
                cur_set.add(item)
        poin_set = cur_set.union(prev_set)
        close_items = cur_set.intersection(prev_set).union(close_items).difference(all_closed_items)
        prev_set = poin_set.difference(cur_set.intersection(prev_set)).difference(close_items)
        if len(close_items) > 0:
            points.append(point)
            all_closed_items = all_closed_items.union(poin_set)
            if all_closed_items == set(segments_ids):
                break

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
