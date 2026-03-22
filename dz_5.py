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




if __name__ == '__main__':
    ex_4()