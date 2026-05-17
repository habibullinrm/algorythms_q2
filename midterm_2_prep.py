import sys
import heapq
from collections import deque
from typing import List, Tuple

graph = {
    1:[2,3],
    2:[3,4,5],
    3:[5,6],
    4:[5,6],
    5:[6],
    6:[]
         }

def bfs(graph, start):
    distances = {start: 0}
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for neighbor in graph[v]:
            if neighbor not in distances:
                distances[neighbor] = distances[v] + 1
                q.append(neighbor)

    return distances

def shortest_path(graph, start, target):
    if start == target:
        return [start]

    parents = {start: None}
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if neighbor not in parents:
                parents[neighbor] = v
                if neighbor == target:
                    path = []
                    while neighbor is not None:
                        path.append(neighbor)
                        neighbor = parents[neighbor]
                    return path[::-1]
                queue.append(neighbor)
    return None

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex in visited:
            continue

        visited.add(vertex)
        print(vertex)

        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)

    return visited

if __name__ == "__main__":
    print(bfs(graph,1))
    print(shortest_path(graph, 1, 5))