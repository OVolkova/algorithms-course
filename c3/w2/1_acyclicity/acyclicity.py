#Uses python3

from typing import Dict, List, Tuple


def transform_edges_to_adjacency_directed(num_of_vertices: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency = {i: [] for i in range(num_of_vertices)}
    for (a, b) in edges:
        adjacency[a].append(b)
    return adjacency


def acyclic(adjacency):
    try:
        cc = GraphCycles(adjacency)
        cc.dfs()
    except CycleException:
        return 1
    return 0


class CycleException(Exception):
    pass


class GraphCycles:
    def __init__(self, adjacency: Dict[int, List[int]]):
        self.vertices = sorted(list(adjacency.keys()))
        self.adjacency = adjacency
        self.visited_vertices = [False] * len(self.vertices)
        self.recurrent_vertices = [False] * len(self.vertices)

    def reset(self):
        self.visited_vertices = [False] * len(self.vertices)
        self.recurrent_vertices = [False] * len(self.vertices)

    def dfs(self):
        for vertex in self.vertices:
            if not self.visited_vertices[vertex]:
                self.explore_cycles(vertex)

    def explore_cycles(self, vertex: int):
        self.visited_vertices[vertex] = True
        self.recurrent_vertices[vertex] = True

        for connected_vertex in self.adjacency[vertex]:
            if not self.visited_vertices[connected_vertex]:
                self.explore_cycles(connected_vertex)
            elif self.recurrent_vertices[connected_vertex]:
                raise CycleException("cycle is found")
        self.recurrent_vertices[vertex] = False


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges_list = []
    for i in range(0, m):
        edges_list.append(list(map(int, input().split())))

    edges_list = [(a-1, b-1) for a, b in edges_list]
    adj = transform_edges_to_adjacency_directed(n, edges_list)

    print(acyclic(adj))
