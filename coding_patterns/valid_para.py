from inspect import stack
from operator import truediv


def valid_parentheses(s):
    # Step 1: mapping of closing to opening brackets
    pairs = {')': '(', ']': '[', '}': '{'}

    stack = []  # Step 2: to store opening brackets

    # Step 3: iterate over each character in s
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

# if ch is an opening bracket → push to stack

# if ch is a closing bracket:
# check if stack is empty or top doesn't match
# otherwise pop from stack

# Step 4: at the end, return True if stack is empty, else False
