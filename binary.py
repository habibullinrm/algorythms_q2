import numpy as np


def binary_search(arr:list[int], key:int, low, high) -> int:
    while low <= high:
        mid = (low + high) // 2

        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            return mid+1

    return low



if __name__ == "__main__":
    rng = np.random.default_rng(seed=42)
    arr = rng.integers(0, 10, size=10)
    print(arr)

    for unsorted_index in range(1, len(arr)):
        j = unsorted_index - 1
        x = arr[unsorted_index]

        loc = binary_search(arr, x, 0, j)

        while j >= loc:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
        print(arr, "Последний отсортированный элемент:", arr[unsorted_index],
              "Вставляемый элемент:", x)
    print(arr)


