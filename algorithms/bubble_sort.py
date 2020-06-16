def bubble_sort(arr):
    """Time complexity: O(n^2) - worst and average, O(n) - best, 
     Auxiliary space complexity - O(1)
    """

    for i in range(len(arr)):
        sorted = True
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            break
    return arr


if __name__ == "__main__":
    print(bubble_sort([2, 4, 3, 2, 1, 6, 7, 3, 8]))
