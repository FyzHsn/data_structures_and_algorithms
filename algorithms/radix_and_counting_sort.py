def count_sort(arr):
    """Time complexity: O(n), Auxiliary space complexity: O(n)"""

    max_val = max(arr)

    num_count = [0 for i in range(max_val + 1)]
    for element in arr:
        num_count[element] += 1

    nums_of_items_before = 0
    for idx, count in enumerate(num_count):
        num_count[idx] = nums_of_items_before
        nums_of_items_before += count

    sorted_arr = [None] * len(arr)
    for element in arr:
        sorted_arr[num_count[element]] = element
        num_count[element] += 1

    return sorted_arr


def radix_sort(arr):
    """Time complexity: O(), Auxiliary space complexity: O()"""

    

if __name__ == "__main__":
    print(count_sort([1, 4, 1, 2, 7, 5, 2]))
