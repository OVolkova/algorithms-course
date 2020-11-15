#Uses python3

from typing import Dict, List, Tuple
import queue


def transform_edges_to_adjacency(num_of_vertices: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency = {i: [] for i in range(num_of_vertices)}
    for (a, b) in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    return adjacency


def distance(adjacency, first_node, second_node):
    cc = Graph(adjacency)
    return cc.get_nodes_distance(first_node, second_node)


class Graph:
    def __init__(self, adjacency: Dict[int, List[int]]):
        self.vertices = sorted(list(adjacency.keys()))
        self.adjacency = adjacency

    def get_nodes_distance_full_bfs(self, start, end):
        vertices_level = self.bfs(start)
        return vertices_level[end]

    def bfs(self, start_node):
        visited = {}
        nodes_queue = queue.Queue()
        nodes_queue.put(start_node)
        visited[start_node] = 0
        while not nodes_queue.empty():
            node = nodes_queue.get()
            level = visited[node]
            for connected_node in self.adjacency[node]:
                if connected_node not in visited.keys():
                    nodes_queue.put(connected_node)
                    visited[connected_node] = level
        return {k: visited.get(k, -1) for k in self.vertices}

    def get_nodes_distance(self, start_node, end_node):
        if start_node == end_node:
            return 0

        visited = {}
        nodes_queue = queue.Queue()
        nodes_queue.put(start_node)
        visited[start_node] = 0
        while not nodes_queue.empty():
            node = nodes_queue.get()
            level = visited[node] + 1
            for connected_node in self.adjacency[node]:
                if connected_node not in visited.keys():
                    nodes_queue.put(connected_node)
                    visited[connected_node] = level
                    if connected_node == end_node:
                        return level
        return -1


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges_list = []
    for i in range(0, m):
        edges_list.append(list(map(int, input().split())))
    x, y = list(map(int, input().split()))

    edges_list = [(a-1, b-1) for a, b in edges_list]
    adj = transform_edges_to_adjacency(n, edges_list)
    x, y = x - 1, y - 1
    print(distance(adj, x, y))
