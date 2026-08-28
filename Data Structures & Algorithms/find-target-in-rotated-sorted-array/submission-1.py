class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r=m
        d = l
        r = n - 1
        if target >= nums[d] and target <=nums[r]:
            l = d
            r = n - 1
        else:
            l = 0
            r = d
        while l <=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r  = m - 1
            else:
                l = m + 1
        return -1