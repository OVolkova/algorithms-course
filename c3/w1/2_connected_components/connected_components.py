#Uses python3


from typing import Dict, List, Tuple


def transform_edges_to_adjacency(num_of_vertices: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency = {i: [] for i in range(num_of_vertices)}
    for (a, b) in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    return adjacency


class ConnectedComponents:
    def __init__(self, adjacency: Dict[int, List[int]]):
        self.vertices = sorted(list(adjacency.keys()))
        self.adjacency = adjacency
        self.component_count = 0
        self.components = {v: None for v in self.vertices}
        self.visited_vertices = []

    def reset(self):
        self.component_count = 0
        self.visited_vertices = []

    def dfs(self):
        for vertex in self.vertices:
            if vertex not in self.visited_vertices:
                self.explore(vertex)
                self.component_count += 1

    def explore(self, vertex: int):
        self.visited_vertices.append(vertex)
        self.components[vertex] = self.component_count
        for connected_vertex in self.adjacency[vertex]:
            if connected_vertex not in self.visited_vertices:
                self.explore(connected_vertex)


def number_of_components(adjacency,):
    cc = ConnectedComponents(adjacency)
    cc.dfs()
    return cc.component_count


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges_list = []
    for i in range(0, m):
        edges_list.append(list(map(int, input().split())))

    edges_list = [(a - 1, b - 1) for a, b in edges_list]
    adj = transform_edges_to_adjacency(n, edges_list)

    print(number_of_components(adj))
