import sys
import heapq
from typing import List, Tuple

def ex_3():
s = list(map(int, input().strip().split()))
p = list(map(int, input().strip().split()))

result = []
br = [0] * (len(s) + len(p) + 1)

merge_list = p
merge_list.append(0)
merge_list.extend(s)
print(merge_list)
for i in range(0, len(merge_list) - 1):
    if merge_list[i + 1] * merge_list[br[i]] > 0:
        print(merge_list[i + 1] * merge_list[br[i]])
        br[i + 1] = br[i] + 1
    else:
        j = br[br[i] - 1]
        while j > 0 & merge_list[j] * merge_list[i + 1] <= 0:
            j = br[br[j] - 1]
        if merge_list[i + 1] * merge_list[j] > 0:
            br[i + 1] = br[j] + 1
    print(br)

    pass


if __name__ == '__main__':
    ex_3()
