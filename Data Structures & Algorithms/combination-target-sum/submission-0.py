class Solution:
    def comsum(self,nums,target,result,temp,s,i):
        if i == len(nums):
            if s == target:
                result.append(temp[:])
                return
            else:
                return
        if s > target:
            return 
        temp.append(nums[i])
        s+=nums[i]
        self.comsum(nums,target,result,temp,s,i)
        v = temp.pop()
        s-=v
        self.comsum(nums,target,result,temp,s,i+1)
        return result

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = self.comsum(nums,target,[],[],0,0)
        return ans