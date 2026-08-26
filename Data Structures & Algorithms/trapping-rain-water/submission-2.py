class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        leftmax,rightmax = height[l],height[r]
        ans = 0
        while  l < r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(height[l],leftmax)
                ans+=leftmax - height[l]
            else:
                r-=1
                rightmax = max(height[r],rightmax)
                ans+=rightmax - height[r]
        return ans 