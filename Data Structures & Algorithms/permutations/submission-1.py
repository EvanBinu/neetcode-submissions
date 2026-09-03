class Solution:
    def permut(self,nums,result,temp,i,visited):
        if len(temp) == len(nums):
            result.append(temp[:])
            return 
        for i in range(len(nums)):
            if visited[i]:
                continue
            temp.append(nums[i])
            visited[i] = 1
            self.permut(nums,result,temp,i+1,visited)
            temp.pop()
            visited[i] = 0
        return result
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permut(nums,[],[],0,[0]*len(nums))