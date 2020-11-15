#Uses python3

from typing import Dict, List, Tuple


def transform_edges_to_adjacency_directed(num_of_vertices: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency = {i: [] for i in range(num_of_vertices)}
    for (a, b) in edges:
        adjacency[a].append(b)
    return adjacency


def toposort(adjacency):
    cc = GraphOrder(adjacency)
    return cc.get_order()


class GraphOrder:
    def __init__(self, adjacency: Dict[int, List[int]]):
        self.vertices = sorted(list(adjacency.keys()))
        self.adjacency = adjacency

        self.visited_vertices = [False] * len(self.vertices)
        self.order_count = 0
        self.post_order = [-1] * len(self.vertices)
        self.pre_order = [-1] * len(self.vertices)

    def reset(self):
        self.visited_vertices = [False] * len(self.vertices)
        self.order_count = 0
        self.post_order = [-1] * len(self.vertices)
        self.pre_order = [-1] * len(self.vertices)

    def get_order(self):
        self.dfs()
        initial_post_order = [x for x, y in sorted(list(enumerate(self.post_order)), key=lambda x: x[1], reverse=True)]
        self.reset()
        self.dfs_with_post_order(initial_post_order)
        post_order = [x for x, y in sorted(list(enumerate(self.post_order)), key=lambda x: x[1], reverse=True)]
        return post_order

    def dfs(self):
        for vertex in self.vertices:
            if not self.visited_vertices[vertex]:
                self.explore(vertex)

    def dfs_with_post_order(self, post_order):
        self.visited_vertices = [False] * len(self.vertices)
        for vertex in post_order:
            if not self.visited_vertices[vertex]:
                self.explore(vertex)

    def explore(self, vertex: int):
        self.visited_vertices[vertex] = True
        self.pre_order[vertex] = self.order_count
        self.order_count +=1

        for connected_vertex in self.adjacency[vertex]:
            if not self.visited_vertices[connected_vertex]:
                self.explore(connected_vertex)

        self.post_order[vertex] = self.order_count
        self.order_count +=1


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges_list = []
    for i in range(0, m):
        edges_list.append(list(map(int, input().split())))

    edges_list = [(a-1, b-1) for a, b in edges_list]
    adj = transform_edges_to_adjacency_directed(n, edges_list)

    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

