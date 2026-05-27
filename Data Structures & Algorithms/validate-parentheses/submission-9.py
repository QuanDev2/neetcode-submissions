class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        opens = ['(', '[', '{']
        comps = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i, char in enumerate(s):
            if char in opens:
                stack.append(char)
            else:
                if not stack or char != comps[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0