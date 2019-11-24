# python3
import sys
from collections import defaultdict


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    counts = defaultdict(int)
    for point in starts:
        counts[point] += 1
    for point in ends:
        counts[point+1] -= 1

    counts = sorted(counts.items(), key=lambda x: x[0])
    total_counts = 0
    sorted_points = sorted(enumerate(points), key=lambda x: x[1])

    current = 0
    for j in range(0, len(counts)):
        segment, count = counts[j]
        if current == len(points):
            break
        for i in range(current, len(points)):
            point_index, point = sorted_points[i]
            current = i+1
            if point < segment and j == 0:
                continue
            elif point < segment and j != 0:
                cnt[point_index] = total_counts
            elif point == segment:
                cnt[point_index] = total_counts+count
            elif point > segment:
                current = i
                break

        total_counts += count

    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
