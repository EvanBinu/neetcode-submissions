class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mcnt = 0
        cnt = 0
        for x in s:
            if x - 1 not in s:
                curr = x
                cnt = 1
                while curr + 1 in s:
                    curr+=1
                    cnt+=1
            mcnt = max(mcnt,cnt)
        return mcnt
                

