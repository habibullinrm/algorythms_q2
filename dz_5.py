import numpy as np



def prefix_function(s: str)->list[int]:
    n = len(s)
    pi = [0] * n

    for i in range(1, n):
        k = pi[i-1]

        while k > 0 and s[i] != s[k]:
            k = pi[k-1]
        
        if s[i] == s[k]:
            k += 1
        
        pi[i] = k
    
    return pi


def kmp():
    s = input()
    t = input()
    combination = t + '#' + s 
    pi = prefix_function(combination)

    m = len(t)
    result = []

    for i in range(m+1, len(combination)):
        if pi[i] == m:
            result.append(i - 2 * m)
    
    return ' '.join(map(str, result))

def ex_2()->int:
    # k - иероглифы, n- кол-во строк, m - столбцы
    k, n, m = [int(x) for x in input().split()]

    letters = []
    for _ in range(k):
        letter = []
        for _ in range(n):
            letter.append(input().strip())
        letters.append(letter)
    
    uniqs = set()

    for i in range(n):
        for j in range(m):
            uniq = tuple(letters[c][i][j] for c in range(k))
            uniqs.add(uniq)

    return len(uniqs)


def ex_3():
    p = input().strip()
    s = input().strip()
    m, n = len(p), len(s)
    combination = p + '#' + s

    pi_1 = prefix_sufix_func(combination)
    pref = [min(pi_1[m + 1 + i], m) for i in range(n)]

    combination_2 = p[::-1] + '#' + s[::-1]
    pi_2 = prefix_sufix_func(combination_2)
    suf = [min(pi_2[m + 1 + (n - 1 - i)], m) for i in range(n)]

    result = []
    for i in range(n - m + 1):
        l = pref[i]
        r = suf[i + m - 1]
        if l + r >= m - 1:
            result.append(i + 1)
    
    print(len(result))
    if result:
        print(*result)
    else:
        print()
        

def boot_algo(s: str) -> int:
    ss = s + s
    n = len(ss)
    f = [-1] * n
    k = 0 
    for j in range(1, n):
        sj = ss[j]
        i = f[j - 1 - k]
        while i != -1 and sj != ss[k + i + 1]:
            if sj < ss[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != ss[k + i + 1]:
            if sj < ss[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k

def ex_4():
    s = input().strip()
    n = len(s)

    best = boot_algo(s)
    min_rot = (s + s)[best:best + n]

    z = prefix_sufix_func(min_rot + '#' + s + s)
    count = sum(1 for i in range(n) if z[n + 1 + i] >= n)

    print(count)

def vagner_fisher(s:str, t:str):
    n = len(s)
    m = len(t)

    dp = [[0 for j in range(0, m+1)] for i in range(0, n+1)]
    

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    
    return dp[n][m]


def ex_4_2():
    s = input().strip()
    n = len(s)

    # префикс-функция
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    period = n - pi[n - 1]
    print(n // period if n % period == 0 else 1)

def ex_5():
    s = input().strip()
    n = len(s)

    trie = [{}]
    count = 0

    for i in range(n):
        node = 0
        for k in range(i, n):
            c = s[k]
            children = trie[node]
            nxt = children.get(c)
            if nxt is None:
                trie.append({})
                nxt = len(trie) - 1
                children[c] = nxt
                count += 1
            node = nxt

    print(count)

def ex_5_2():
    s = input().strip()
    n = len(s)
    base = 131
    mod = (1 << 61) - 1

    h = [0] * (n + 1)
    pw = [1] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * base + ord(s[i])) % mod
        pw[i + 1] = pw[i] * base % mod

    seen = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            seen.add((h[j] - h[i] * pw[j - i]) % mod)

    print(len(seen))

def ex_5_3():
    s = input().strip()
    n = len(s)

    sa = sorted(range(n), key=lambda i: s[i:])

    rank = [0] * n
    for k, i in enumerate(sa):
        rank[i] = k

    lcp_sum = 0
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp_sum += h
            if h > 0:
                h -= 1
        else:
            h = 0

    print(n * (n + 1) // 2 - lcp_sum)

def over_len(a: str, b: str) -> int:
    if not a or not b:
        return 0
    tail = a[max(0, len(a) - len(b)):]
    pattern = b + '#' + tail
    f = prefix_function(pattern)
    return f[-1]

def prefix_sufix_func(s: str)-> list[int]:
    n = len(s)
    pi = [0] * n
    l = r =0
    
    for i in range(1, n):
        if i < r:
            pi[i] = min(r-i, pi[i-l])
        
        while i + pi[i] < n and s[pi[i]] == s[i + pi[i]]:
            pi[i] += 1
        
        if i + pi[i] > r:
            l, r = i, i + pi[i]
    
    return pi

def ex_6():
    n = int(input())
    words = input().split()

    result = words[0]
    for i in range(1, n):
        w = words[i]
        ov = over_len(result, w)
        result += w[ov:]

    print(result)

def z_function(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

def ex_7_2():
    S = input().strip()
    T = input().strip()

    n = len(T)
    Z = z_function(S + '#' + T)
    offset = len(S) + 1

    prev = [None] * (n + 1)
    prev[0] = -1         
    max_reach = 0

    for j in range(n):
        if j > max_reach:
            break         

        z_val = Z[offset + j]       
        new_reach = j + z_val

        if new_reach > max_reach:
            for k in range(max_reach + 1, min(new_reach, n) + 1):
                prev[k] = j          # k достигнута из j
            max_reach = new_reach

    if prev[n] is None:
        print("Yes")
    else:
        parts = []
        pos = n
        while pos > 0:             
            p = prev[pos]
            parts.append(T[p:pos])
            pos = p
        parts.reverse()
        print("No")
        print(' '.join(parts))

if __name__ == '__main__':
    ex_7_2()
