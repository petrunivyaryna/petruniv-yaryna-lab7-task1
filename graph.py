# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.
"""Develop functions that will perform actions on graphs."""
def get_graph_from_file(file_name):
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    graph = []
    with open(file_name, 'r', encoding = 'utf-8') as file:
        for line in file.readlines():
            content = line.strip().split(',')
            graph.append([int(content[0]), int(content[1])])
    return graph

def to_edge_dict(edge_list):
    """
    (list) -> (dict)
    Convert a graph from list of edges to dictionary of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    graph = {}
    for edges in edge_list:
        v_1, v_2 = edges
        if v_1 not in graph:
            graph[v_1] = [v_2]
        else:
            graph[v_1].append(v_2)
            graph[v_1].sort()
        if v_2 not in graph:
            graph[v_2] = [v_1]
        else:
            graph[v_2].append(v_1)
            graph[v_2].sort()
    return graph

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    in_vertex = edge[1]
    out_vertex = edge[0]
    in_edges = graph.get(in_vertex)
    return out_vertex in in_edges

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph. 
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    >>> add_edge({1: [2], 2: [1]}, (1, 3))
    {1: [2, 3], 2: [1], 3: [1]}
    >>> add_edge({1: [2], 2: [1]}, (3, 1))
    {1: [2, 3], 2: [1], 3: [1]}
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (6, 7))
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1], 6: [7], 7: [6]}
    """
    v_1, v_2 = edge
    if v_1 not in graph:
        graph[v_1] = [v_2]
    else:
        graph[v_1].append(v_2)
    if v_2 not in graph:
        graph[v_2] = [v_1]
    else:
        graph[v_2].append(v_1)
    return graph

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    >>> del_edge({1: [2], 2: [1]}, (1, 3))
    {1: [2], 2: [1]}
    >>> del_edge({1: [2], 2: [1]}, (3, 1))
    {1: [2], 2: [1]}
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 5))
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    v_1, v_2 = edge
    if v_1 in graph and v_2 in graph and v_2 in graph[v_1] and v_1 in graph[v_2]:
        graph[v_1].remove(v_2)
        graph[v_2].remove(v_1)
    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    >>> add_node({1: [2], 2: [1]}, 1)
    {1: [2], 2: [1]}
    """
    if node not in graph:
        graph[node] = []
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        del graph[node]
    for v_1 in range(1, len(graph)):
        if node in graph[v_1]:
            graph[v_1].remove(node)
    return graph

def convert_to_dot(graph):
    """ 
    (dict) -> (None)
    
    Save the graph to a file in a DOT format.
    >>> convert_to_dot({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})
    """
    pass
