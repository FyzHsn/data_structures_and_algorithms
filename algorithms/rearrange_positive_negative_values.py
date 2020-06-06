def rearrange_positive_and_negative(a):
    """Time Complexity: O(n), Auxilary Space Complexity: O(n)"""

    rearranged = [None] * len(a)
    pos_idx = 0
    neg_idx = len(a) - 1
    for element in a:
        if element >= 0:
            rearranged[pos_idx] = element
            pos_idx += 1
        else:
            rearranged[neg_idx] = element
            neg_idx -=1
    return rearranged


if __name__ == "__main__":
    test_inputs = [[1, 1, -1, -2, 1, 2, 0],
                   [1, 1, 1],
                   [-1, -1],
                   []]

    for input in test_inputs:
        print(rearrange_positive_and_negative(input))
