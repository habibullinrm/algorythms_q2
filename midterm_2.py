import sys
import heapq
from collections import deque
from typing import List, Tuple

def ex_1():
    n, m = map(int, input().strip().split())
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = []

    for i in range(m):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
    q = deque()
    q.append(1)
    visited = set()

    while q:
        v = q.popleft()
        visited.add(v)

        for neighbor in graph[v]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return ' '.join(map(str, sorted(list(visited))))

def ex_2():
    v = int(input().strip())
    matrix = []

    for i in range(v):
        matrix.append(list(map(int, input().strip().split())))

    for k in range(v):
        for i in range(v):
            for j in range(v):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    for i in range(v):
        print(' '.join(map(str, matrix[i])))

    return matrix

def check_neighbor(i, j, matrix: List[List[int]]):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return False
    return True

def get_neighbors(m, i, j, matrix: List[List[int]]) -> List[List[int]]:
    neighbors = []

    if check_neighbor(i - 1 ,j , matrix) and matrix[i-1][j] != 1:
        neighbors.append((i-1) * m + j)
    if check_neighbor(i + 1 ,j , matrix) and matrix[i+1][j] != 1:
        neighbors.append((i+1) * m + j)
    if check_neighbor(i, j - 1, matrix) and matrix[i][j-1] != 1:
        neighbors.append(i * m + (j-1))
    if check_neighbor(i, j + 1, matrix) and matrix[i][j+1] != 1:
        neighbors.append(i * m + (j+1))

    return neighbors

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


def ex_3():
    n, m = map(int, input().strip().split())
    init_matrix = []
    for i in range(n):
        init_matrix.append(list(map(int, input().strip().split())))

    graph = dict()
    targets = list()
    for i in range(n):
        for j in range(m):
            graph[i*m + j] = []
            if init_matrix[i][j] == 1:
                continue
            if init_matrix[i][j] == 2:
                targets.append(i*m + j)
            graph[i * m + j] = get_neighbors(m, i, j, init_matrix)

    distances = bfs(graph, 0)

    best = 10**5
    for target in targets:
        if distances[target] < best:
            best = distances[target]

    return best

if __name__ == "__main__":
    print(ex_3())