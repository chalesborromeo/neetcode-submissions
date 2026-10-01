class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(', ']':'[', '}':'{'}
        p_stack = []
        for c in s:
            if c in parentheses:
                if p_stack and p_stack[-1] == parentheses[c]:
                    p_stack.pop()
                else:
                    return False
            else:
                p_stack.append(c)
        return True if not p_stack else False