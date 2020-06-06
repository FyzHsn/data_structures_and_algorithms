def find_first_non_repeating_int(l):
    """Time Complexity: O(n), Auxillary Space Complexity: O(n)"""

    repeat_record_dict = dict()
    for element in l:
        if element in repeat_record_dict:
            repeat_record_dict[element] = True
        else:
            repeat_record_dict[element] = False
    for element in l:
        if not repeat_record_dict[element]:
            return element
    return None


if __name__ == "__main__":
    a = [1, 1, 2, 2]
    b = [1]
    c = [1, 1]
    d = [1, 2, 1]
    e = []

    print(find_first_non_repeating_int(a))
    print(find_first_non_repeating_int(b))
    print(find_first_non_repeating_int(c))
    print(find_first_non_repeating_int(d))
    print(find_first_non_repeating_int(e))
