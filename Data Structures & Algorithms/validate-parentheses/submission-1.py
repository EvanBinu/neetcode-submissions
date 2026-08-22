class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {']' : '[','}' : '{',')':'('}
        for x in s:
            if x in "[{(":
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] != map[x]:
                        return False
                    else:
                        stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False