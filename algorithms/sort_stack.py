from collections import deque


def insert_at_bottom(s, element):
    if len(s) == 0 or element >= s[-1]:
        s.append(element)
    else:
        top = s.pop()
        insert_at_bottom(s, element)
        s.append(top)
    return


def sort_stack(s):
    """Time Complexity: O(n^2), Auxilary Space Complexity: O(n)"""

    if len(s) == 0:
        return 
    top = s.pop()
    sort_stack(s)
    insert_at_bottom(s, top)
    return s


if __name__ == "__main__":
    test_cases = [[1, 5, 2, 6],
                  [7, 3, 4, 1],
                  [1]]
    for input in test_cases:
        stack = deque()
        for item in input:
            stack.append(item)
        print(sort_stack(stack))
                   
