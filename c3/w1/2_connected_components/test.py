
from typing import List, Tuple
import numpy as np
import networkx as nx
from networkx.algorithms.components import number_connected_components
from connected_components import transform_edges_to_adjacency, number_of_components


def transform_matrix_to_edges(matrix) -> List[Tuple[int, int]]:
    edges = []
    for i in range(0, matrix.shape[0]):
        for j in range(i+1, matrix.shape[1]):
            if matrix[i, j]:
                edges.append((i, j))
    return edges


def nx_number_of_components(num_of_vertices, edges):
    G = nx.Graph()
    G.add_nodes_from(list(range(0, num_of_vertices)))
    G.add_edges_from(edges)
    return number_connected_components(G)


if __name__ == '__main__':
    while True:
        n = np.random.randint(2, 10, 1)[0]
        matrix = np.random.randint(0, 2, (n, n))
        np.fill_diagonal(matrix, 0)
        matrix = np.tril(matrix) + np.tril(matrix, -1).T
        edges_list = transform_matrix_to_edges(matrix)

        other = nx_number_of_components(n,  edges_list)
        adj = transform_edges_to_adjacency(n, edges_list)
        mine = number_of_components(adj)
        if other == mine:
            print(n, edges_list, 'OK', other)
        else:
            print(n, edges_list, other, mine)
            break
