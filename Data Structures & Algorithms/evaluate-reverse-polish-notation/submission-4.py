class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if x == '+':
                    c = a+b
                elif x == '-':
                    c = a-b
                elif x == '*':
                    c = a*b
                else:
                    c = int(a/b)
                stack.append(c)
            else:
                stack.append(int(x))
        return stack[-1]