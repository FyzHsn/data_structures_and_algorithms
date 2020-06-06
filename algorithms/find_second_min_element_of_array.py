def find_second_min_element(l):
    """Time Complexity: O(n), Auxillary Space Complexity: O(1)"""

    min = None
    sec_min = None
    for element in l:
        if min is None or element < min:
            sec_min = min
            min = element
        elif sec_min is None and element > min:
            sec_min = element
    return sec_min

if __name__ == "__main__":
    test = [[7, 3, 2, 4, 1, 1],
            [1, 1],
            [1],
            [1, 2],
            []]

    for l in test:
        print(f"{str(l)}: {find_second_min_element(l)}")
