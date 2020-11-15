# python3


from collections import deque


def max_sliding_window(sequence, m):
    result = []
    n = len(sequence)
    Qi = deque()

    # Process first k (or first window) elements of array
    for i in range(m):
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    for i in range(m, n):
        result.append(sequence[Qi[0]])

        # Remove the elements which are out of this window
        while Qi and Qi[0] <= i - m:
            Qi.popleft()

        # Remove all elements smaller than the currently being added element
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    result.append(sequence[Qi[0]])
    return result


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

