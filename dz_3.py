import sys
import heapq
from typing import List, Tuple

import numpy as np
from pandas.io.formats.format import return_docstring

def magic_counts(n:int)-> int:
    # рекурсивно, но так получваем неверное решение
    result = 0
    print(n)
    if n == 1:
        return result
    elif n % 3 == 0:
        result +=1
        return result + magic_counts(n//3)
    elif n % 2 == 0:
        result +=1
        return result + magic_counts(n//2)
    else:
        result += 1
        return result + magic_counts(n - 1)

def magic_counts2(n:int)->int:
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    print(dp)
    return(dp[n])

def exam_comb(n:int)->int:
    dp = [0] * (n+1)
    if n ==0:
        return dp[n]
    dp[1] = 2
    if n == 1:
        return dp[n]
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i-2]

    return dp[n]

def prof_sneip(n:int)->int:
    dp = [0] * (n+1)
    if n ==0:
        return 1
    if n == 1:
        return 3
    dp[0] = 1
    dp[1] = 3
    for i in range(2, n+1):
        dp[i] = 2*(dp[i-1] + dp[i-2])

    return dp[n]

def chess(n:int, m:int)->int:
    dp =  [[0]*n for _ in range(m)]

    if n < 1 or m < 1:
        return 0

    for i in range(0, n):
        for j in range(0, m):
            if i==0 and j==0:
                dp[0][0] = 1
            if i >= 2 and j >= 1:
                dp[i][j] += dp[i-2][j-1]
            if i >= 1 and j >= 2:
                dp[i][j] += dp[i-1][j-2]

    return int(dp[n-1][m-1] % 1000000007)


def mandragora(n:int, coords:List[int])->int:
    coords.sort()
    INF = float('inf')
    dp = [[INF, INF] for _ in range(n)]

    dp[0][0] = 0
    dp[0][1] = INF

    for i in range(1, n):
        cost = coords[i] - coords[i - 1]
        dp[i][1] = min(dp[i-1][0] + cost, dp[i-1][1] + cost)
        dp[i][0] = dp[i-1][1]

    return dp[n - 1][1]

if __name__ == '__main__':
    n = int(input())
    coords = [int(x) for x in input().strip().split()]

    # print(coords)
    print(mandragora(n, coords))

