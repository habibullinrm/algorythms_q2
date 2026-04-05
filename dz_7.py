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

if __name__ == '__main__':
    hash_code()
