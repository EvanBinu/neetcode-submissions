class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0]*n
        stack.append(0)
        for i in range(1,n):
            if temperatures[stack[-1]] < temperatures[i]:
                while temperatures[stack[-1]] < temperatures[i]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(i)
            else:
                stack.append(i)
        return result
