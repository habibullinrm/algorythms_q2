import sys
import heapq
from typing import List, Tuple

import numpy as np
from pandas.io.formats.format import return_docstring

def harry_and_novp():
    n1 = int(input())
    s1 = [int(x) for x in input().strip().split()]
    n2 = int(input())
    s2 = [int(x) for x in input().strip().split()]

    dp = [0] * n2
    base = [-1] * n2

    for i in range(0, n1):
        cur = 0
        cur_idx = -1
        for j in range(0, n2):
            if s1[i] == s2[j] and cur + 1 > dp[j]:
                dp[j] = cur + 1
                base[j] = cur_idx
            if s1[i] > s2[j] and dp[j] > cur:
                cur = dp[j]
                cur_idx = j
        # print(dp)
    best = max(dp)
    print(best)

    if best == 0:
        print(' ')
    else:
        ans_j = dp.index(best)
        novp = []
        j = ans_j
        while j != -1:
            novp.append(s2[j])
            j = base[j]
        novp.reverse()
        print(' '.join(map(str, novp)))
    return

def hogvarts_bag():
    n, m = map(int, input().split())
    mass = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    dp = [0] * (m + 1)
    choice = [[False] * (m + 1) for _ in range(n)]

    for i in range(n):
        for ms in range(m, mass[i] - 1, -1):
            if dp[ms - mass[i]] + cost[i] > dp[ms]:
                dp[ms] = dp[ms - mass[i]] + cost[i]
                choice[i][ms] = True

    res = []
    ms = m
    for i in range(n - 1, -1, -1):
        if choice[i][ms]:
            res.append(i + 1)
            ms -= mass[i]

    res.reverse()
    print(*res)

def ex_3():
    n = int(input())
    s = [int(x) for x in input().strip().split()]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if s[i] > s[j]:
                dp[i] += dp[j]
    print(sum(dp))

def ex_4():
    s = input()
    r = s[::-1]
    n = len(s) // 2 + 1

    prev = [0] * (n + 1)
    for i in range(n):
        cur = [0] * (n + 1)
        for j in range(n):
            if s[i] == r[j]:
                cur[j+1] = prev[j] + 1
            else:
                cur[j+1] = max(prev[j + 1], cur[j])
        prev = cur
    print(prev)
    print(n - prev[n])
    return

if __name__ == '__main__':
import numpy as np

s = input()
r = s[::-1]

s_bytes = np.frombuffer(s.encode(), dtype=np.uint8)
r_bytes = np.frombuffer(r.encode(), dtype=np.uint8)
n = len(r_bytes)
prev = np.zeros(n + 1, dtype=np.int32)
for i in range(n):
    matches = np.where(s_bytes[i] == r_bytes, prev[:n] + 1, 0)
    run_max = np.maximum.accumulate(matches)
    prev[1:] = np.maximum(prev[1:], run_max)
print(n - prev[n])