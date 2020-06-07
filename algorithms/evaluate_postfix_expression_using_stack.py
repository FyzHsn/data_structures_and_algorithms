import sys
sys.path.append('/Users/faiyaz/Code/data_structures_and_algorithms')
print(sys.path)

from linear_data_structures.stack import Stack


def evaluate_postfix_expressions(expr):
    """Time Complexity: O(n), Auxilary Space Complexity: O(n)"""

    s = Stack()
    for element in expr:
        if element not in set({'+', '-', '*', '/'}):
            s.push(element)
        else:
            b = s.pop()
            a = s.pop()
        if element == '+':
            s.push(a + b)
        elif element == '-':
            s.push(a - b)
        elif element == '*':
            s.push(a * b)
        elif element == '/':
            s.push(a * 1.0 / b)
    return s.pop()


if __name__ == "__main__":
    test_cases = [[4, 5, 7, 2, '+', '-', '*'],
                  [3, 4, '+', 2, '*', 7, '/'],
                  [5, 7, '+', 6, 2, '-', '*']]
    for case in test_cases:
        print(evaluate_postfix_expressions(case))
