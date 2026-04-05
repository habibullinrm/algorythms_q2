import numpy as np
import typing
import string

def build_hash(s: str, base: int, mod: int):
    n = len(s)
    prefs = [0] * (n + 1)
    pows = [1] * (n + 1)

    for i, ch in enumerate(s):
      prefs[i + 1] = (prefs[i] * base + ord(ch)) % mod
      pows[i + 1] = (pows[i] * base) % mod

    return prefs, pows

def sub_hash(pref, pows, l: int, r: int, mod: int):
    return (pref[r] - pref[l] * pows[r - l]) % mod


# 1
def hash_code():
    k = int(input().strip())
    n = 1000
    base = 31
    '''
    H(s) = (s0 * base ** (n-1) + ... + sn)
    1. минимальная строка с длиной 2: hash(XY) = hash(AB)
    2. ord(X) * 31 + ord(Y) = ord(A)*31 + ord(B)
        31 * (ord(X) - ord(A)) = ord(B) - ord(Y)
    3. пусть ord(X) - ord(A) = 1, тогда ord(B) = 31 + ord(Y)
    X = 81 - Q
    A = 80 - P
    Y = 81 - Q
    B = 112 - p
    QQ = Pp
    '''

    n = k.bit_length()
    result = []

    for i in range(k):
        parts = []
        for j in range(n-1, -1, -1):
            if (i >> j) & 1:
                parts.append('QQ')
            else:
                parts.append('Pp')
        result.append(''.join(parts))

    print("\n".join(result))


#2 Сравнения подстрок

def sub_string_compare():
    s = input().strip()
    m = int(input().strip())
    arr = []
    for _ in range(m):
        arr.append([int(x) for x in input().strip().split()])

    base = 911382323
    mod = 1000000001
    prefs, pows = build_hash(s, base, mod)
    for idx_list in arr:
        h1 = sub_hash(prefs, pows, idx_list[0] - 1, idx_list[1], mod)
        h2 = sub_hash(prefs, pows, idx_list[2] - 1, idx_list[3], mod)
        if h1 != h2:
            print('No')
        elif s[idx_list[0] - 1:idx_list[1]] == s[idx_list[2] - 1:idx_list[3]]:
            print('Yes')
        else:
            print('No')

def cycle_equation():
    s = input().strip()
    t = input().strip()

    n, m = len(s), len(t)
    if n != m:
        print('NO')
        return

    base = 911382323
    mod = 1000000001
    prefs1, pows1 = build_hash(s, base, mod)
    prefs2, pows2 = build_hash(t, base, mod)
    for i in range(0, n):
        hl1 = sub_hash(prefs1, pows1, 0, i, mod)
        hr1 = sub_hash(prefs1, pows1, i, n, mod)
        hl2 = sub_hash(prefs2, pows2, 0, n-i, mod)
        hr2 = sub_hash(prefs2, pows2, n-i, n, mod)

        if hl1 != hr2 and hr1 != hl2:
            continue
        else:
            if s[0:i] == t[n - i:n] and s[i:n] == t[0:n - i]:
                print('YES')
                return

    print('NO')
    return

def equal_sums():
    n, s = [int(x) for x in input().strip().split()]
    numbers = [int(x) for x in input().strip().split()]

    n_dict = {}
    count = 0
    for numb in numbers:
        comp = s - numb
        if comp in n_dict:
            count += n_dict[comp]
        n_dict[numb] = n_dict.get(numb, 0) + 1

    print(count)
    return

def cube_equals():
    n = int(input().strip())
    count = {}

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[i**3 + j**3] = count.get(i**3 + j**3, 0) + 1

    result = 0
    for k in count.values():
        result += k ** 2

    print(result)
    return

def four_equals():
    n = int(input().strip())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = [int(x) for x in input().strip().split()]
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    ab = {}
    for a in A:
        for b in B:
            ab[a + b] = ab.get(a + b, 0) + 1
    count = 0
    for c in C:
        for d in D:
            count += ab.get(-(c + d), 0)

    print(count)
    return

def build_hash_arr(arr, base, mod):
    n = len(arr)
    prefs = [0] * (n + 1)
    pows  = [1] * (n + 1)
    for i, v in enumerate(arr):
        prefs[i+1] = (prefs[i] * base + v) % mod
        pows[i+1]  = (pows[i]  * base)     % mod
    return prefs, pows

def cubes():
    n, m = [int(x) for x in input().strip().split()]
    s = input().strip()
    arr = [int(x) for x in s.split()]
    base = 911382323
    mod = 1000000001
    prefs, pows = build_hash_arr(arr, base, mod)
    prefs_rev, pows_rev = build_hash_arr(arr[::-1], base, mod)
    result = []
    result.append(n)
    for i in range(1, n//2 +1):
        h1 = sub_hash(prefs, pows, 0, i, mod)
        h2 = sub_hash(prefs_rev, pows, n - i * 2, n - i, mod)
        if h1 != h2:
            continue
        else:
            if arr[0:i] == arr[2 * i - 1:: -1][:i]:
                result.append(n - i)
        palindrome_check = arr[0:i] == arr[2 * i - 1::-1][:i]
        print(
            f"i={i}, arr[0:{i}]={arr[0:i]}, reverse={arr[2 * i - 1::-1][:i]}, h1={h1}, h2={h2}, palindrome={palindrome_check}")
    res = result[::-1]
    print(res)
    return

def sort_string():
    s = input().strip()
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord('a')] += 1
    result = []
    for i in range(26):
        result.append(chr(ord('a') + i) * count[i])
    print(''.join(result))




if __name__ == '__main__':
    sort_string()
