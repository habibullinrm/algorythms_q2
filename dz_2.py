import sys
import heapq
from typing import List, Tuple

from pandas.io.formats.format import return_docstring


def sum(a, b):
	if b == 0:
		return a
	a += 1
	b -= 1
	return sum(a,b)


def hearch(n:int, arr: list):
    sorted_arr = sorted(arr, reverse=True)
    i = 0
    while i < n and sorted_arr[i] > i:
        i += 1
        print(i)
    return i


def calculator(n: int, arr: List, comission = 0.05) -> float:
    heapq.heapify(arr)
    sum = 0

    while n > 1:
        new = heapq.heappop(arr) + heapq.heappop(arr)
        sum += new*comission
        heapq.heappush(arr, new)
        n -= 1
    return sum


def merge(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def merge_k_sorted(arr_list):
    """Слияние K отсортированных массивов за O(N log K) через попарное слияние."""
    arrays = list(arr_list)
    while len(arrays) > 1:
        next_level = []
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                next_level.append(merge(arrays[i], arrays[i + 1]))
            else:
                next_level.append(arrays[i])
        arrays = next_level
    return arrays[0] if arrays else []


# heap-based O(N log K) — для сравнения
def func_4(arr_list):
    heap = []
    for i, arr in enumerate(arr_list):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    result = []
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(arr_list[arr_idx]):
            next_val = arr_list[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
    return result

def hoare_partition(a, l, r):
    pivot = a[(l + r) // 2]
    i, j = l - 1, r + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

def quick_sort(a, l=0, r=None):
    if r is None:
        r = len(a) - 1
    if l >= r:
        return
    p = hoare_partition(a, l, r)
    quick_sort(a, l, p)
    quick_sort(a, p + 1, r)

def sort_by_last_digit(arr:List[int])->List[int]:
    '''
    сортирует элементы массива по возрастанию последней цифры десятичной записи чисел.
    :param arr: list
    :return: list
    '''
    heap = []
    for i in range(len(arr)):
        heap.append(tuple([arr[i] % 10, i, arr[i]]))
    heapq.heapify(heap)
    result = []
    while heap:
        elem = heapq.heappop(heap)
        result.append(elem[2])
    return result

class TaskTracker:
    def __init__(self):
        self.tasks = []
        self.task_id = -1
        heapq.heapify(self.tasks)

    def getTaskId(self):
        return self.task_id

    def getTask(self):
        if self.tasks:
            task = heapq.heappop(self.tasks)
            return task[1]
        return -1

    def addTask(self, task_priority:int):
        self.task_id += 1
        heapq.heappush(self.tasks, tuple([-task_priority, self.task_id]))
        return 'ok'


if __name__ == '__main__':
    task_tracker = TaskTracker()

    while True:
        command = list(map(int, input().split()))
        if command[0] == 1:
            print(task_tracker.getTask())
            print(task_tracker.tasks)
        elif command[0] == 2:
            print(task_tracker.addTask(command[1]))
            print(task_tracker.tasks)
        elif command[0] == 3:
            break
        else:
            print('неизвестная команда')


