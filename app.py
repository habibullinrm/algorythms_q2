import numpy as np
import dz_1

if __name__ == "__main__":
    rng = np.random.default_rng(seed=42)
    rng2 = np.random.default_rng(seed=37)
    max_iters = 100
    success = 1

    for i in range(max_iters):
        len_arr = rng.integers(1, 10, size=1)
        arr = rng2.integers(0, 20, size=len_arr)

        true_sorted_arr = sorted(arr)
        algo_sorted_arr = dz_1.selection_sort(arr, len_arr)
        if not np.allclose(true_sorted_arr, algo_sorted_arr):
            print(f'true-sorted: {true_sorted_arr}, algo-sorted: {algo_sorted_arr}')
            success = 0

    if success:
        print(f'success: {success}')