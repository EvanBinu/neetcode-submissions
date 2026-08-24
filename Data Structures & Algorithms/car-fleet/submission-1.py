class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            d = [position[i],speed[i],(target-position[i])/speed[i]]
            arr.append(d)
        arr.sort(key = lambda x:x[0],reverse=True)
        stack=[]
        for x in arr:
            if len(stack)==0:
                stack.append(x[2])
            else:
                if stack[-1] < x[2]:
                    stack.append(x[2])
        return len(stack)
