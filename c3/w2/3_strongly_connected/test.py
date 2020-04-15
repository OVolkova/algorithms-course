
from typing import List, Tuple
import numpy as np
import networkx as nx
from networkx.algorithms.components.strongly_connected import number_strongly_connected_components
from strongly_connected import number_of_strongly_connected_components


def transform_matrix_to_edges_directed(matrix) -> List[Tuple[int, int]]:
    edges = []
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            if matrix[i, j]:
                edges.append((i, j))
    return edges


def nx_number_of_strongly_connected_components(num_of_vertices, edges):
    G = nx.DiGraph()
    G.add_nodes_from(list(range(0, num_of_vertices)))
    G.add_edges_from(edges)
    return number_strongly_connected_components(G)


if __name__ == '__main__':
    while True:
        n = np.random.randint(2, 10, 1)[0]
        matrix = np.random.randint(0, 2, (n, n))
        np.fill_diagonal(matrix, 0)
        edges_list = transform_matrix_to_edges_directed(matrix)

        other = nx_number_of_strongly_connected_components(n,  edges_list)

        mine = number_of_strongly_connected_components(n, edges_list)
        if mine == other:
            print(n, other, 'OK', edges_list)
        else:
            print(n, other, mine, edges_list)
            break
