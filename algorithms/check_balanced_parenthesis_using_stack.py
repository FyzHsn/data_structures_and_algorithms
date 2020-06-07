from collections import deque


def check_parenthesis_balance(p):
    """Time Complexity: O(n), Auxilary Space Complexity: O(n)"""

    stack = deque()
    bracket_pair_dict = {'}': '{', ']': '[', ')': '('}
    open_brackets = set({'{', '[', '('})
    for bracket in p:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket not in open_brackets:
            if not stack:
                return False
            elif bracket_pair_dict[bracket] != stack[-1]:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False  


if __name__ == "__main__":
    test_cases = ['([((){})])', '(((})))', '{[(())]}']
    for parenthesis in test_cases:
        print(check_parenthesis_balance(parenthesis))

