# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                opening = stack.pop() if stack else None
                if closeToOpen[c] != opening:
                    return False
        
        return not stack
            