from math import inf
from multiprocessing import heap

import numpy as np
import sys


def ex_1():
    data = sys.stdin.read().split()
    idx = 0
    v = int(data[idx])
    idx += 1

    INF = float('inf')
    m = [[INF] * v for _ in range(v)]
    for i in range(v):
        for j in range(v):
            x = int(data[idx])
            idx += 1
            if x >= 0:
                m[i][j] = x

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = m[i][k] + m[k][j]

    result = 0
    for i in range(v):
        for j in range(v):
            if m[i][j] != INF and m[i][j] > result:
                result = m[i][j]
    print(result)

def floyd_warshall(v, m):
    next = [[-1] * (v + 1) for _ in range(v + 1)]
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] =  m[i][k] + m[k][j]
                    next[i][j] = k
    return m, next


def floyd_warshall_2(v, m):
    parent = [[-1] * (v + 1) for _ in range(v + 1)]
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i != j and m[i][j] != inf:
                parent[i][j] = i

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = m[i][k] + m[k][j]
                    parent[i][j] = parent[k][j]

    return m, parent

def floyd_warshall_3(v, m, parent):
    for k in range(1, v + 1):
        mk = m[k]
        pk = parent[k]
        for i in range(1, v + 1):
            mik = m[i][k]
            if mik == inf:
                continue
            mi = m[i]
            pi = parent[i]
            for j in range(1, v + 1):
                mkj = mk[j]
                if mkj == inf:
                    continue
                nd = mik + mkj
                if nd < mi[j]:
                    mi[j] = nd
                    pi[j] = pk[j]
    return m, parent


def ex_2():
    v, e = map(int, input().strip().split())
    m = [[inf] * (v + 1) for _ in range(v + 1)]
    for i in range(1, v + 1):
        m[i][i] = 0
    parent = [[-1] * (v + 1) for _ in range(v + 1)]

    for _ in range(e):
        row = list(map(int, input().strip().split()))
        u, w, weight = row[0], row[1], row[2]
        if weight < m[u][w]:
            m[u][w] = weight
            parent[u][w] = u
    m, parent = floyd_warshall_3(v, m, parent)

    for i in range(1, v + 1):
        if m[i][i] < 0:
            cur = i
            for _ in range(v):
                cur = parent[i][cur]
            cycle = [cur]
            x = parent[i][cur]
            while x != cur:
                cycle.append(x)
                x = parent[i][x]
            cycle.reverse()

            print("LOOP")
            print(len(cycle))
            print(*cycle)
            return

    print("NO LOOP")
    for i in range(1, v + 1):
        row = []
        for j in range(1, v + 1):
            row.append("INF" if m[i][j] == inf else str(m[i][j]))
        print(*row, "")



import heapq

def ex_3():
    # diykstra
    n, s, f = map(int, input().strip().split())
    matrix = []
    for _ in range (n):
        matrix.append(list(map(int, input().strip().split())))
    s -= 1
    f -= 1

    dist = {v: float('inf') for v in range(n)}
    visited = set()
    dist[s] = 0
    heap = [(0, s)]

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in enumerate(matrix[u]):
            if w < 0:
                continue
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    if (dist[f] == float('inf')):
        print(-1)
    else:
        print(dist[f])
    return



def ex_4():
    v, e = map(int, input().strip().split())
    s, t = map(int, input().strip().split())
    adj = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b, w = map(int, input().strip().split())
        adj[a].append((b, w))
        adj[b].append((a, w))

    dist = {i: float('inf') for i in range(v+1)}
    dist[s] = 0
    visited = set()
    parent = [-1] * (v + 1)
    heap = [(0, s)]

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for i, w in adj[u]:
            if dist[u] + w < dist[i]:
                dist[i] = dist[u] + w
                parent[i] = u
                heapq.heappush(heap, (dist[i], i))

    if dist[t] == float('inf'):
        print(-1)
    else:
        print(dist[t])
        path = []
        cur = t
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        print(len(path))
        print(*[x for x in path])


import heapq
import sys


def ex_5():
    data = sys.stdin.read().split()
    it = iter(data)

    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    C = int(next(it))

    cities = [int(next(it)) for _ in range(K)]

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s = int(next(it))
        e = int(next(it))
        t = int(next(it))
        graph[s].append((e, t))
        graph[e].append((s, t))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[C] = 0
    heap = [(0, C)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    result = [(dist[city], city) for city in cities]
    result.sort()

    out = []
    for d, city in result:
        out.append(f"{city} {d}")
    print(*out, sep='\n')


import sys
import heapq

def ex_6():
    data = sys.stdin.read().split()
    idx = 0
    v = int(data[idx])
    idx += 1

    INF = float('inf')
    m = [[0] * (v + 1) for _ in range(v + 1)]
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            m[i][j] = int(data[idx])
            idx += 1

    parent = [[-1] * (v + 1) for _ in range(v + 1)]
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if m[i][j] < INF:
                parent[i][j] = i

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = m[i][k] + m[k][j]
                    parent[i][j] = parent[k][j]

    neg_vertex = -1
    for i in range(1, v + 1):
        if m[i][i] < 0:
            neg_vertex = i
            break

    if neg_vertex == -1:
        print("NO")
        return

    cur = neg_vertex
    for _ in range(v):
        cur = parent[neg_vertex][cur]

    cycle = [cur]
    x = parent[neg_vertex][cur]
    while x != cur:
        cycle.append(x)
        x = parent[neg_vertex][x]
    cycle.append(cur)
    cycle.reverse()

    print("YES")
    print(len(cycle))
    print(*cycle)


import sys
import heapq
def ex_7():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    sx = int(data[idx]) - 1
    idx += 1
    sy = int(data[idx]) - 1
    idx += 1
    tx = int(data[idx]) - 1
    idx += 1
    ty = int(data[idx]) - 1
    idx += 1

    grid = []
    for i in range(N):
        grid.append(data[idx])
        idx += 1

    def cost(ch):
        if ch == '.': return 1
        if ch == 'W': return 2
        return -1

    INF = float('inf')
    size = N * M
    dist = [INF] * size
    prev_dir = [''] * size

    start = sx * M + sy
    target = tx * M + ty
    dist[start] = 0
    dirs = [(-1, 0, 'N'), (1, 0, 'S'), (0, 1, 'E'), (0, -1, 'W')]

    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == target:
            break
        x = u // M
        y = u % M
        for dx, dy, ch in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                c = cost(grid[nx][ny])
                if c < 0:
                    continue
                nd = d + c
                v = nx * M + ny
                if nd < dist[v]:
                    dist[v] = nd
                    prev_dir[v] = ch
                    heapq.heappush(heap, (nd, v))

    if dist[target] == INF:
        print(-1)
        return

    path = []
    cur = target
    while cur != start:
        ch = prev_dir[cur]
        path.append(ch)
        x = cur // M
        y = cur % M
        if ch == 'N':
            px, py = x + 1, y
        elif ch == 'S':
            px, py = x - 1, y
        elif ch == 'E':
            px, py = x, y - 1
        else:
            px, py = x, y + 1
        cur = px * M + py

    path.reverse()
    print(dist[target])
    print(*path, sep='')


import sys
import heapq
def ex_8():
    pass



if __name__ == "__main__":
    ex_2()