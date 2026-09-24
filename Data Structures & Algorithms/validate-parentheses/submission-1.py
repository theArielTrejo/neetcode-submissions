class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combos = {")": "(", "}": "{", "]" : "["}
        for symbol in s:
            if symbol in combos:
                if stack and stack[-1] == combos[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return True if not stack else False
                