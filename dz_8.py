import numpy as np
import typing
import string
import queue


def ex_1():
    n_e, n_v = map(int, input().strip().split())

    v = [[] for _ in range(0, n_e)]
    for i in range(1, n_v + 1):
        a ,b = map(int, input().strip().split())
        v[a - 1].append(b)
        v[b - 1].append(a)
    print(' '.join([str(len(x)) for x in v]))

def ex_2():
    n, m = map(int, input().strip().split())

    v = [[] for _ in range(0, m)]
    matrix = [[0 for _ in range(0, n)] for _ in range(0, n)]

    for _ in range(0, m):
        i ,j = map(int, input().strip().split())
        matrix[i - 1][j - 1] += 1
    for i in range(n):
        print(' '.join([str(x) for x in matrix[i]]))

def ex_3():
    v = int(input().strip())
    matrix = [[0 for _ in range(0, v)] for _ in range(0, v)]
    for i in range(v):
        matrix[i] = list(map(int, input().strip().split()))
    start, end = map(int, input().strip().split())
    start -= 1
    end -= 1

    q = queue.Queue()
    dist = [-1] * (v)
    dist[start] = 0
    q.put(start)

    while not q.empty():
        el = q.get()
        for i, item in enumerate(matrix[el]):
            if dist[i] == -1 and item == 1:
                dist[i] = dist[el] + 1
                q.put(i)

    print(str(dist[end]))

from collections import deque

def get_neighbors(n):
    d = [n // 1000, (n // 100) % 10, (n // 10) % 10, n % 10]
    result = []

    if d[0] < 9:
        result.append((d[0] + 1) * 1000 + d[1] * 100 + d[2] * 10 + d[3])

    if d[3] > 1:
        result.append(d[0] * 1000 + d[1] * 100 + d[2] * 10 + (d[3] - 1))

    result.append(d[3] * 1000 + d[0] * 100 + d[1] * 10 + d[2])

    result.append(d[1] * 1000 + d[2] * 100 + d[3] * 10 + d[0])

    return result

def ex_4():
    x = int(input().strip())
    y = int(input().strip())

    dist = {x: 0}
    parent = {x: None}
    q = deque([x])

    while q:
        v = q.popleft()
        if v == y:
            break
        for u in get_neighbors(v):
            if u not in dist:
                dist[u] = dist[v] + 1
                parent[u] = v
                q.append(u)

    path = []
    cur = y
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(len(path))
    print(' '.join(map(str, path)))

def ex_5():
    n = int(input().strip())
    x1, y1 = map(int, input().strip().split())
    x2, y2 = map(int, input().strip().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    dist = [[-1] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    dist[x1][y1] = 0
    q = deque([(x1, y1)])

    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            break
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                parent[nx][ny] = (x, y)
                q.append((nx, ny))

    path = []
    cx, cy = x2, y2
    while (cx, cy) != (x1, y1):
        path.append((cx + 1, cy + 1))
        cx, cy = parent[cx][cy]
    path.append((x1 + 1, y1 + 1))
    path.reverse()

    print(dist[x2][y2])
    for px, py in path:
        print(px, py)

def ex_6():
    n, m = map(int, input().split())

    next_node = n
    adj = [[] for _ in range(n + m)]

    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1; v -= 1
        if c == 1:
            adj[u].append(v)
            adj[v].append(u)
        else:
            adj[u].append(next_node)
            adj[next_node].append(u)
            adj[next_node].append(v)
            adj[v].append(next_node)
            next_node += 1

    dist = [-1] * (n + m)
    dist[0] = 0
    q = deque([0])

    while q:
        v = q.popleft()
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)

    print(dist[n - 1])

def ex_7():
    n, m = map(int, input().split())
    rev = [[] for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        rev[b - 1].append((a - 1, t))

    dist = [[-1, -1] for _ in range(n)]
    dist[n - 1][0] = 0
    dist[n - 1][1] = 0

    q = deque()
    q.append((n, 1))
    q.append((n, 2))

    while q:
        v, t = q.popleft()
        other = 3 - t
        for u, edge_type in rev[v]:
            if edge_type == other and dist[u][other - 1] == -1:
                dist[u][other - 1] = dist[v][t - 1] + 1
                q.append((u, other))

    result = []
    for i in range(n - 1):
        d1, d2 = dist[i]
        if d1 == -1 and d2 == -1:
            result.append('-1')
        elif d1 == -1:
            result.append(str(d2))
        elif d2 == -1:
            result.append(str(d1))
        else:
            result.append(str(min(d1, d2)))

    print(' '.join(result))

if __name__ == '__main__':
    ex_7()
