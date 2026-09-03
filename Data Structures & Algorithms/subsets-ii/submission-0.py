class Solution:
    def sub(self,nums,result,temp,i):
        if i == len(nums):
            result.append(temp[:])
            return
        
        temp.append(nums[i])
        self.sub(nums,result,temp,i+1)
        temp.pop()
        while i+1<len(nums) and nums[i] == nums[i+1]:
            i+=1
        self.sub(nums,result,temp,i+1)
        return result
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.sub(nums,[],[],0)
        