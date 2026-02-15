import numpy as np


def bubble_sort(arr, len_arr):
    counter = 0
    for i in range(1, len(arr)):
        for j in range (0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter += 1
    return arr

def selection_sort(arr, len_arr):
    counter = 0
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            counter += 1
    return arr

def sum_enumns(arr, len_arr):
    result = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            result += arr[i]
    return result

def manual_pow(num):
    low = 0
    high = num
    result = num / 2
    epsilon = 1e-6

    while abs(result ** 2 - num) > epsilon:
        if result ** 2 < num:
            low = result
            result = (low + high) / 2
        else:
            high = result
            result = (low + high) / 2
    return result

def binary_search(arr:list[int], key:int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            return mid

    return low

def left_bound(arr, key):
    """Первый индекс, где arr[i] >= key"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def right_bound(arr, key):
    """Первый индекс, где arr[i] > key"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
    return low


def fast_search_in_arr(arr, low, high):
    if low > high:
        low, high = high, low
    i = 0
    result = 0
    while i < len_arr and arr[i] < low:
        result += 1
        i += 1
    j = len(arr) - 1
    while arr[j] > high and i <= j:
        result += 1
        j -= 1
    print(len(arr) - result)

def manual_pow_and_square(num):
    def func(x):
        return x ** 2 + x ** 0.5
    low = 0
    high = num
    result = num / 2
    epsilon = 1e-6

    while abs(func(result) - num) > epsilon:
        if func(result) < num:
            low = result
            result = (low + high) / 2
        else:
            high = result
            result = (low + high) / 2
    return result

def find_pairs(arr, x):
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] <= x:
                result += 1
    return result

def merge_two_row():
    x = int(input())

    result = 0
    count = 0
    i, j = 1, 1

    while count < x:
        b = j ** 2
        a = i ** 3

        if a == b:
            count += 1
            i += 1
            j += 1
            result = a
        elif a > b:
            count += 1
            j += 1
            result = b
        else:
            count += 1
            i += 1
            result = a
    return result

def calculate_combination_count():
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    n_comb = 0

    for i in range(n):
        j = n - 1
        while ((arr[j] - arr[i]) > r) and (j > i):
            n_comb += 1
            j -= 1

    print(n_comb)

if __name__ == '__main__':
    for _ in range(5):
        rng = np.random.default_rng()
        num = rng.integers(0, 100)
        print(num)
        print(manual_pow_and_square(num))

    n, x = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    print(find_pairs(arr, x))

