
from typing import List, Tuple
import numpy as np
import networkx as nx
from networkx.algorithms.dag import all_topological_sorts
from networkx.algorithms.cycles import find_cycle
from networkx.exception import NetworkXNoCycle
from toposort import transform_edges_to_adjacency_directed, toposort


def transform_matrix_to_edges_directed(matrix) -> List[Tuple[int, int]]:
    edges = []
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            if matrix[i, j]:
                edges.append((i, j))
    return edges


def nx_toposort(num_of_vertices, edges):
    G = nx.DiGraph()
    G.add_nodes_from(list(range(0, num_of_vertices)))
    G.add_edges_from(edges)
    return list(all_topological_sorts(G))


def nx_acyclic(num_of_vertices, edges):
    G = nx.DiGraph()
    G.add_nodes_from(list(range(0, num_of_vertices)))
    G.add_edges_from(edges)
    try:
        cycle = find_cycle(G)
    except NetworkXNoCycle:
        return True
    return False


if __name__ == '__main__':
    while True:
        n = np.random.randint(2, 10, 1)[0]
        matrix = np.random.randint(0, 2, (n, n))
        np.fill_diagonal(matrix, 0)
        edges_list = transform_matrix_to_edges_directed(matrix)
        if nx_acyclic(n,  edges_list):
            other = nx_toposort(n,  edges_list)
            adj = transform_edges_to_adjacency_directed(n, edges_list)
            mine = toposort(adj)
            if mine in other:
                print(n, other, 'OK', edges_list)
            else:
                print(n, other, mine, edges_list)
                break
