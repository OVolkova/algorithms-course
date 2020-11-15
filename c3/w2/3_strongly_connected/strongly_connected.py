#Uses python3

import sys
from typing import Dict, List, Tuple
sys.setrecursionlimit(200000)


def transform_edges_to_adjacency_directed(num_of_vertices: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency = {i: [] for i in range(num_of_vertices)}
    for (a, b) in edges:
        adjacency[a].append(b)
    return adjacency


def number_of_strongly_connected_components(n, edges_list):
    cc = Graph(n, edges_list)
    cc.count_strongly_connected_components()
    return cc.component_count


class Graph:
    def __init__(self, num_of_vertices: int, edges: List[Tuple[int, int]]):
        self.adjacency = transform_edges_to_adjacency_directed(num_of_vertices, edges)
        self.reverse_adjacency = transform_edges_to_adjacency_directed(num_of_vertices, [(b, a) for a, b in edges])
        self.vertices = sorted(list(self.adjacency.keys()))

        self.visited_vertices = [False] * len(self.vertices)
        self.order_count = 0
        self.post_order = [-1] * len(self.vertices)
        self.pre_order = [-1] * len(self.vertices)
        self.connected_components = []
        self.component_count = 0
        self.components = [-1] * len(self.vertices)

    def reset(self):
        self.visited_vertices = [False] * len(self.vertices)
        self.order_count = 0
        self.post_order = [-1] * len(self.vertices)
        self.pre_order = [-1] * len(self.vertices)
        self.component_count = 0
        self.components = [-1] * len(self.vertices)

    def count_strongly_connected_components(self):
        self.dfs_reverse()
        reverse_post_order = [x for x, y in sorted(list(enumerate(self.post_order)), key=lambda x: x[1], reverse=True)]
        self.reset()
        self.dfs_with_post_order(reverse_post_order)

    def dfs_reverse(self):
        for vertex in self.vertices:
            if not self.visited_vertices[vertex]:
                self.explore(vertex, self.reverse_adjacency)

    def dfs_with_post_order(self, post_order):
        self.visited_vertices = [False] * len(self.vertices)
        for vertex in post_order:
            if not self.visited_vertices[vertex]:
                self.explore(vertex, self.adjacency)
                self.component_count += 1

    def explore(self, vertex: int, adjacency):
        self.visited_vertices[vertex] = True
        self.pre_order[vertex] = self.order_count
        self.order_count += 1
        self.components[vertex] = self.component_count

        for connected_vertex in adjacency[vertex]:
            if not self.visited_vertices[connected_vertex]:
                self.explore(connected_vertex, adjacency)

        self.post_order[vertex] = self.order_count
        self.order_count +=1


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges_list = []
    for i in range(0, m):
        edges_list.append(list(map(int, input().split())))

    edges_list = [(a-1, b-1) for a, b in edges_list]

    print(number_of_strongly_connected_components(n, edges_list))
