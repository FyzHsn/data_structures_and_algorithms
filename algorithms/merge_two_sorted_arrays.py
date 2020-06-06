def merge_sorted_arrays(a_1, a_2):
    n_1, n_2 = len(a_1), len(a_2)
    if n_1 == 0:
        return a_2
    elif n_2 == 0:
        return a_1
    idx_1, idx_2 = 0, 0
    merged = []
    while idx_1 < n_1 and idx_2 < n_2:
        if a_1[idx_1] <= a_2[idx_2]:
            merged.append(a_1[idx_1])
            idx_1 += 1
        else:
            merged.append(a_2[idx_2])
            idx_2 += 1
    if idx_1 == n_1:
        merged += a_2[idx_2:]
    if idx_2 == n_2:
        merged += a_1[idx_1:]
    return merged



if __name__ == "__main__":
    print(merge_sorted_arrays([1, 3, 4, 5, 7, 8, 9, 10], [2, 5, 6]))
    print(merge_sorted_arrays([1], [2]))
    print(merge_sorted_arrays([1], []))
