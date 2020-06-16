def insertion_sort(arr):
    """Time complexity: O(n^2), Auxiliary space complexity: O(1)"""

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    print(insertion_sort([3, 4, 1, 7, 5, 6, 2, 3, 4, 1]))
