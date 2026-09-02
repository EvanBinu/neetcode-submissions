class Solution:
    def subset(self,nums,result,temp,i):
        if i == len(nums):
            result.append(temp[:])
            return
        temp.append(nums[i])
        self.subset(nums,result,temp,i+1)
        temp.pop()
        self.subset(nums,result,temp,i+1)
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = self.subset(nums,[],[],0)
        return ans