class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        n = len(heights)
        stack =[]
        for i in range(n+1):
            while stack and (i == n or heights[i] <= heights[stack[-1]]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                maxarea =max(maxarea,h*w)
            stack.append(i)
        return maxarea