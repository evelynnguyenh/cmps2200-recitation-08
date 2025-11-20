import heapq
from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    dist = {v: (float("inf"), float("inf")) for v in graph}
    dist[source] = (0, 0)

    # priority queue: (weight, edges, node)
    pq = [(0, 0, source)]

    while pq:
        cur_w, cur_edges, u = heapq.heappop(pq)

        # skip outdated entries
        if (cur_w, cur_edges) > dist[u]:
            continue

        # graph[u] is a SET of tuples (v, w)
        for (v, w) in graph[u]:
            new_w = cur_w + w
            new_edges = cur_edges + 1

            if (new_w, new_edges) < dist[v]:
                dist[v] = (new_w, new_edges)
                heapq.heappush(pq, (new_w, new_edges, v))

    return dist
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent = {}
    visited = set([source])
    q = deque([source])

    while q:
        u = q.popleft()

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)

    return parent


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []

    node = destination
    while node in parents:
        node = parents[node]
        path.append(node)

    path.reverse()

    # join without arrows, only nodes, e.g. ['s','b','c'] -> "sbc"
    return "".join(path)