import sys
import heapq
from typing import List, Tuple

import numpy as np

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

def ex_1():
    data = sys.stdin.read().split()
    idx = 0
    n1 = int(data[idx]); idx += 1
    s1 = [int(data[idx + i]) for i in range(n1)]; idx += n1
    n2 = int(data[idx]); idx += 1
    s2 = [int(data[idx + i]) for i in range(n2)]; idx += n2

    dp = [0] * n2
    chain = [None] * n2 

    for i in range(n1):
        cur_len = 0
        cur_node = None
        for j in range(n2):
            if s2[j] == s1[i]:
                if cur_len + 1 > dp[j]:
                    dp[j] = cur_len + 1
                    chain[j] = (j, cur_node)
            elif s2[j] < s1[i]:
                if dp[j] > cur_len:
                    cur_len = dp[j]
                    cur_node = chain[j]

    max_len = max(dp) if n2 else 0
    result = []
    if max_len > 0:
        max_j = max(range(n2), key=lambda j: dp[j])
        node = chain[max_j]
        while node is not None:
            j_idx, prev = node
            result.append(s2[j_idx])
            node = prev
        result.reverse()

    print(max_len)
    print(*result)



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

def ex_4_2():
    S = input().strip()
    n = len(S)
    T = S[::-1]

    prev = [0] * (n + 1)

    for i in range(1, n + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                curr[j] = prev[j - 1]
            else:      
                curr[j] = min(prev[j], prev[j - 1]) + 1 
        prev = curr

    lps = prev[n]
    print(n - lps)

def ex_4_3():
    s = input().strip()
    n = len(s)
    prev = [0] * (n + 1)  
    curr = [0] * (n + 1)  
    for i in range(n - 1, -1, -1):
        curr[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j - 1] + 2
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev
    return n - prev[n - 1]

import sys


def ex_5():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    L = int(data[1])
    x = list(map(int, data[2:2 + n]))

    count = 0
    i = 0
    while i < n:
        count += 1
        right = x[i] + L          
        while i < n and x[i] <= right:
            i += 1                 
    print(count)

def ex_6():
    pass

def ex_7():
    n = int(input())

    dp = [0] + [1] * 9                       

    for _ in range(n - 1):
        nxt = [0] * 10
        nxt[0] = dp[0] + dp[1]               
        for d in range(1, 9):
            nxt[d] = dp[d - 1] + dp[d] + dp[d + 1]
        nxt[9] = dp[8] + dp[9]               
        dp = nxt

    print(sum(dp))

def ex_8():
    data = sys.stdin.read().split()
    c_ins, c_del, c_rep = int(data[0]), int(data[1]), int(data[2])
    s = data[3] if len(data) > 3 else ""
    t = data[4] if len(data) > 4 else ""

    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i * c_del
    for j in range(1, m + 1):
        dp[0][j] = j * c_ins

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + c_rep,  
                    dp[i - 1][j]     + c_del,  
                    dp[i][j - 1]     + c_ins, 
                )

    print(dp[n][m])


if __name__ == '__main__':
    ex_8()