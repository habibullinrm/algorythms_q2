from scipy.stats import false_discovery_control


def ex_1():
    n_v, n_e = map(int, input().split())
    v = [[] for _ in range(n_v + 1)]
    for i in range(n_e):
        f, t = map(int, input().split())
        v[f].append(t)
        v[t].append(f)

    visited = [0] * (n_v + 1)
    components = []

    for i in range(1, n_v + 1):
        if visited[i] == 0:
            component = []
            dfs(i, v, visited, component)
            components.append(component)

    print(len(components))
    for comp in components:
        comp.sort()
        print(len(comp))
        print(*comp)

def dfs(start, graph, visited, component):
    stack = [start]
    visited[start] = 1
    while stack:
        node = stack.pop()
        component.append(node)
        for u in graph[node]:
            if visited[u] == 0:
                visited[u] = 1
                stack.append(u)

def ex_2():
    n_v, n_e = map(int, input().split())
    v = [[] for _ in range(n_v + 1)]
    for i in range(n_e):
        f, t = map(int, input().split())
        v[f].append(t)

    color = [0] * (n_v + 1)

    for i in range(1, n_v + 1):
        if color[i] == 0:
            if dfs2(i, v, color):
                return 1  # нашли цикл хоть где-то → сразу выходим

    return 0

def dfs2(node, graph, color):
    color[node] = 1
    for u in graph[node]:
        if color[u] == 1:
            return 1
        if color[u] == 0 and dfs2(u, graph, color):
            return 1
    color[node] = 2
    return 0

def ex_3():
    n_v, n_e = map(int, input().split())
    v = [[] for _ in range(n_v + 1)]
    for i in range(n_e):
        f, t = map(int, input().split())
        v[f].append(t)

    color = [0] * (n_v + 1)
    order = []

    for i in range(1, n_v + 1):
        if color[i] == 0:
            if dfs3(i, v, color, order):
                print(-1)
                return

    print(*order[::-1])

def dfs3(node, graph, color, order):
    color[node] = 1
    for u in graph[node]:
        if color[u] == 1:
            return 1
        if color[u] == 0 and dfs3(u, graph, color, order):
            return 1
    color[node] = 2
    order.append(node)
    return 0

def ex_3_1():
    n_v, n_e = map(int, input().split())
    graph = [[] for _ in range(n_v + 1)]
    for _ in range(n_e):
        f, t = map(int, input().split())
        graph[f].append(t)

    color = [0] * (n_v + 1)
    order = []

    for start in range(1, n_v + 1):
        if color[start] != 0:
            continue

        stack = [(start, 0)]
        while stack:
            node, state = stack.pop()

            if state == 1:
                color[node] = 2
                order.append(node)
                continue

            if color[node] != 0:
                continue

            color[node] = 1
            stack.append((node, 1))

            for u in graph[node]:
                if color[u] == 1:
                    print(-1)
                    return
                if color[u] == 0:
                    stack.append((u, 0))

    print(*order[::-1])


def ex_4():
    n_v, n_e = map(int, input().split())
    edges = []
    for _ in range(n_e):
        u, v = map(int, input().split())
        edges.append((u, v))

    perm = list(map(int, input().split()))

    position = [0] * (n_v + 1)
    for idx, vertex in enumerate(perm):
        position[vertex] = idx

    for u, v in edges:
        if position[u] >= position[v]:
            print("NO")
            return
    print("YES")


def ex_5():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)  # -1 = не покрашена

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        if dfs5(start, graph, color):
            print("NO")
            return

    print("YES")

def dfs5(start, graph, color):
    color[start] = 0                # стартовую красим в 0
    stack = [start]
    while stack:
        node = stack.pop()
        for u in graph[node]:
            if color[u] == -1:
                color[u] = 1 - color[node]
                stack.append(u)
            else:
                if color[u] == color[node]:
                    return True
    return False


def ex_6():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    components = []

    for start in range(1, n + 1):
        if visited[start]:
            continue

        component = []
        stack = [start]
        visited[start] = True

        while stack:
            node = stack.pop()
            component.append(node)
            for u in graph[node]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        components.append(component)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(*comp)


def ex_8():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        color[start] = 0
        stack = [start]
        v_count = 0
        edge_sum = 0
        bipartite = True

        while stack:
            node = stack.pop()
            v_count += 1
            edge_sum += len(graph[node])
            for u in graph[node]:
                if color[u] == -1:
                    color[u] = 1 - color[node]
                    stack.append(u)
                elif color[u] == color[node]:
                    bipartite = False

        e_count = edge_sum // 2

        if e_count >= v_count + 1:
            print("YES")
            return
        if e_count >= v_count and bipartite:
            print("YES")
            return

    print("NO")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        ex_8()