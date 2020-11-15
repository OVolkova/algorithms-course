# python3

import sys
import threading
from collections import defaultdict


sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def __init__(self, n, parents):
        self.n = n
        self.tree = self.build_tree(parents)

    @ staticmethod
    def build_tree(parents):
        tree = defaultdict(list)
        for item, parent in enumerate(parents):
            tree[parent].append(item)
        return tree

    def compute_height(self):
        return self.compute_subtree_height(-1, 1, 1)

    def compute_subtree_height(self, node, current_height, max_height):
        for item in self.tree[node]:
            if item in self.tree.keys():
                max_height = max(max_height, self.compute_subtree_height(item, current_height+1, max_height))
            else:
                max_height = max(max_height, current_height)
        return max_height


def main():
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    tree = TreeHeight(n, parents)
    print(tree.compute_height())


threading.Thread(target=main).start()
