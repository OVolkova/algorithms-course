# python3
import sys
from collections import defaultdict


def filter_items(k, candidates, prev_digit, digit):
    f_cond = []
    for c, l in candidates:
        if len(c) > k:
            if int(c[k]) == prev_digit:
                f_cond.append((c, l))
        else:
            # if short+digit bigger than digit_short -> keep short
            if int(c + str(digit)) >= int(str(digit)+c):
                f_cond.append((c, l))

    return f_cond


def make_comparison(k, candidates, first_digit):
    np_digit = None
    nf_digit = None
    has_short = False
    for c, l in candidates:
        if l > k:
            if not np_digit or np_digit < int(c[k]):
                np_digit = int(c[k])
            if (not nf_digit or nf_digit < int(c[k])) and first_digit <= int(c[k]):
                nf_digit = int(c[k])
        if l <= k:
            has_short = True

    return np_digit, nf_digit, has_short


def largest_number(array):
    # arrange elements in stacks by length. elements in each stack should be sorted in reverse order/
    al = defaultdict(list)
    for a in array:
        al[len(str(a))].append(str(a))
    lengths = max(sorted(al.keys()))
    al = {l: sorted(i, reverse=True) for l, i in al.items()}

    # sort elements in stacks
    result = ''
    while True:
        # take first from each stack and select the biggest first digit
        candidates = []
        f_digit = None
        for l, a in al.items():
            if a:
                candidates.append((a[0], l))
                if not f_digit or f_digit < int(a[0][0]):
                    f_digit = int(a[0][0])

        # of all stacks are empty - exit
        if not f_digit:
            break

        # select biggest from taken
        digit = f_digit
        f_cond = filter_items(0, candidates, f_digit, digit)
        for k in range(1, lengths):
            np_digit, nf_digit, has_short = make_comparison(k, f_cond, f_digit)
            if np_digit:
                digit = int(str(digit) + str(np_digit))
            # if have short and next digit smaller than first -> go with that short seq
            if has_short and not nf_digit:
                short = []
                for cond, l in f_cond:
                 if l <= k:
                     short.append((cond, l))
                f_cond = short
                break
            f_cond = filter_items(k, f_cond, np_digit, digit)

        # append to the result
        if f_cond:
            item, minl = sorted(f_cond, key=lambda x: str(x[0]))[0]
            al[minl] = al[minl][1:]
            result += str(item)

    return int(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

