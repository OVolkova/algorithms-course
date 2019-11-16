# python3
import sys


def compute_min_refills(distance, tank, stops, num_refills=0, last_refill=0):

    if not stops:
        if distance - last_refill > tank:
            return -1
        else:
            return num_refills

    all_way_stops = sorted(stops) + [distance]
    for i in range(1, len(all_way_stops)):
        if all_way_stops[i] - last_refill > tank:
            if all_way_stops[i-1] == last_refill:
                return -1
            else:
                num_refills = compute_min_refills(distance,
                                                  tank,
                                                  stops[i-1:],
                                                  num_refills=num_refills+1,
                                                  last_refill=all_way_stops[i-1])
                return num_refills

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

