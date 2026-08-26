class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n -1 
        msum = 0
        s = 0
        while l<r:
            w = min(heights[l],heights[r])
            msum = max(msum,w*(r-l))
            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        return msum