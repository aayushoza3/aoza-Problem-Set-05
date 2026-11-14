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
    ### TODO
    best = {source: (0, 0)}
    frontier = [(0, 0, source)]
    while frontier:
        cost_so_far, hops_so_far, node = heappop(frontier)
        if (cost_so_far, hops_so_far) > best.get(node, (float('inf'), float('inf'))):
            continue
        for neighbor, step in graph[node]:
            candidate = (cost_so_far + step, hops_so_far + 1)
            if candidate < best.get(neighbor, (float('inf'), float('inf'))):
                best[neighbor] = candidate
                heappush(frontier, (candidate[0], candidate[1], neighbor))
    return best
