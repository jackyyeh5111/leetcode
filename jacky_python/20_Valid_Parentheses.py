from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        parentheses_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []
        for token in s:
            if token in "([{":
                stack.append(token)
            elif len(stack) == 0:
                return False
            elif len(stack) > 0:
                if stack[-1] == parentheses_map[token]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0

s = "([)]"
solution = Solution()
print (solution.isValid(s))