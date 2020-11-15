# python3


class Heap:
    def __init__(self, data, n):
        self.data = data
        self.n = n
        self.swaps = []
        self.swaps_counter = 0

    def build_heap(self):
        """Build a heap from ``data`` inplace.

        Returns a sequence of swaps performed by the algorithm.
        """
        half = self.n//2
        for k in range(0, half):
            i = half-k-1
            self.sift_down(i)

    @staticmethod
    def left_child(i):
        return 2*i+1

    @staticmethod
    def right_child(i):
        return 2*i+2

    def sift_down(self, i):
        maxelem = i
        l = self.left_child(i)
        r = self.right_child(i)
        if l < self.n and self.data[l] < self.data[maxelem]:
            maxelem = l
        if r < self.n and self.data[r] < self.data[maxelem]:
            maxelem = r

        if i != maxelem:
            self.swaps.append((i, maxelem))
            self.swaps_counter += 1
            self.data[maxelem], self.data[i] = self.data[i], self.data[maxelem]
            self.sift_down(maxelem)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    heap = Heap(data, n)
    heap.build_heap()

    print(heap.swaps_counter)
    for i, j in heap.swaps:
        print(i, j)


if __name__ == "__main__":
    main()
