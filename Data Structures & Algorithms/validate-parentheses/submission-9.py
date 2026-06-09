class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # will make key, value for us with the value we add to the stack and the value we check:
        close_to_open = {')':'(',']':'[','}':'{'}

        for char in s:
            # if its an open parentesis, add to stack
            if char in "({[":
                stack.append(char)
            # if its close parentesis, we need to make sure its with a open paren that fits him:
            elif char in close_to_open:
                if stack and stack[-1] == close_to_open.get(char):
                    stack.pop()
                else:
                    return False
        return not stack