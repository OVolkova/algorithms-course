#Uses python3


from typing import Dict, List, Tuple
import queue


def transform_edges_to_adjacency(num_of_vertices: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    adjacency = {i: [] for i in range(num_of_vertices)}
    for (a, b) in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    return adjacency


def bipartite(adjacency):
    cc = Graph(adjacency)
    return int(cc.is_bipartite())


class Graph:
    def __init__(self, adjacency: Dict[int, List[int]]):
        self.vertices = sorted(list(adjacency.keys()))
        self.adjacency = adjacency

    def is_bipartite(self):
        visited = {}
        nodes_queue = queue.Queue()
        for start_node in self.vertices:
            if start_node in visited.keys():
                continue
            nodes_queue.put(start_node)
            visited[start_node] = True
            while not nodes_queue.empty():
                node = nodes_queue.get()
                level = not visited[node]
                for connected_node in self.adjacency[node]:
                    if connected_node not in visited.keys():
                        nodes_queue.put(connected_node)
                        visited[connected_node] = level
                    else:
                        if visited[connected_node] != level:
                            return False
        return True


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges_list = []
    for i in range(0, m):
        edges_list.append(list(map(int, input().split())))

    edges_list = [(a-1, b-1) for a, b in edges_list]
    adj = transform_edges_to_adjacency(n, edges_list)
    print(bipartite(adj))
