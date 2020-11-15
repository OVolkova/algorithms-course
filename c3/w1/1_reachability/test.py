
from typing import List, Tuple
import numpy as np
import networkx as nx
from networkx.algorithms import approximation as approx
from reachability import transform_edges_to_adjacency, reach


def transform_matrix_to_edges(matrix) -> List[Tuple[int, int]]:
    edges = []
    for i in range(0, matrix.shape[0]):
        for j in range(i+1, matrix.shape[1]):
            if matrix[i, j]:
                edges.append((i, j))
    return edges


def is_in_range(num_of_vertices, edges, first_node, second_node):
    G = nx.Graph()
    G.add_nodes_from(list(range(0, num_of_vertices)))
    G.add_edges_from(edges)
    if approx.node_connectivity(G, first_node,  second_node) > 0:
        return 1

    return 0


if __name__ == '__main__':
    while True:
        n = np.random.randint(2, 10, 1)[0]
        matrix = np.random.randint(0, 2, (n, n))
        np.fill_diagonal(matrix, 0)
        matrix = np.tril(matrix) + np.tril(matrix, -1).T
        edges_list = transform_matrix_to_edges(matrix)
        x = np.random.randint(0, n, 1)[0]
        while True:
            y = np.random.randint(0, n, 1)[0]
            if x != y:
                break
        other = is_in_range(n,  edges_list, x, y)
        adj = transform_edges_to_adjacency(n, edges_list)
        mine = reach(adj, x, y)
        if other == mine:
            print(n, edges_list, x, y, 'OK', other)
        else:
            print(n, edges_list, x, y, other, mine)
            break
