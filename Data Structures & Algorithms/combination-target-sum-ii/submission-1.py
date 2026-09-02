class Solution:
    def comsum(self,nums,target,result,temp,s,i):
        if s == target:
            result.append(temp[:])
            return 
        if s > target or i >= len(nums):
            return 
        temp.append(nums[i])
        s+=nums[i]
        self.comsum(nums,target,result,temp,s,i+1)
        v = temp.pop()
        s-=v
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        self.comsum(nums,target,result,temp,s,i+1)
        return result
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.comsum(candidates,target,[],[],0,0)
        