class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<=r:
            m = (l+r)//2
            cnt = sum(math.ceil(p/m) for p in piles)
            if cnt <= h:
                r = m - 1
            else:
                l = m + 1
        return l