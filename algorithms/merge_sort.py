def merge_arrays(arr_1, arr_2):
    arr = [None] * (len(arr_1) + len(arr_2))
    idx_1 = idx_2 = 0
    while idx_1 < len(arr_1) and idx_2 < len(arr_2):
        if arr_1[idx_1] < arr_2[idx_2]:
            arr[idx_1 + idx_2] = arr_1[idx_1]
            idx_1 += 1
        else:
            arr[idx_1 + idx_2] = arr_2[idx_2]
            idx_2 += 1
    if idx_2 >= len(arr_2) - 1:
        arr[(idx_1 + idx_2):] = arr_1[idx_1:]
    if idx_1 >= len(arr_1) - 1:
        arr[(idx_1 + idx_2):] = arr_2[idx_2:]
    return arr


def merge_sort(arr):
    """TIme complexity: O(nlog(n)), auxiliary space complexity: O(n)"""
   
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge_arrays(left, right)
    return arr


if __name__ == "__main__":
    print(merge_sort([1, 5, 2, 6, 2, 3, 2, 9, 1]))


