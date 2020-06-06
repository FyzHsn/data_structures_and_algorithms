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
    l_1 = [7, 3, 2, 4, 1, 1]
    l_2 = [1, 1]
    l_3 = [1]
    l_4 = [1, 2]

    print(find_second_min_element(l_1))
    print(find_second_min_element(l_2))
    print(find_second_min_element(l_3))
    print(find_second_min_element(l_4))
