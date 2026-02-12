def binary_search(arr:list[int], key:int) -> int:
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high and not found:
        median_index = (low + high) // 2
        median = arr[median_index]

        if key < median:
            high = median_index - 1
        elif key > median:
            low = median_index + 1
        else:
            found = True
            return median_index

    return -1

if __name__ == "__main__":
    arr = np.linspace(1, 100, 100)
    key = 101

    print(binary_search(arr, key))

