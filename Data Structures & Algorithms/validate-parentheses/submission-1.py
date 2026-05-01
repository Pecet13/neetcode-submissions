class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            elif char in pairs.values():
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char != pairs[top]:
                    return False
        return len(stack) == 0