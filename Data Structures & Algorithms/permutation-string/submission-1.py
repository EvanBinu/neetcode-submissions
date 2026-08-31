class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = {}
        for x in s1:
            target[x] = target.get(x,0)+1
        freq = {}
        n = len(s1)
        for i in range(n):
            freq[s2[i]] = freq.get(s2[i],0)+1
        if freq == target:
            return True
        l = 0
        for i in range(n,len(s2)):
            freq[s2[l]]-=1
            if freq[s2[l]] == 0:
                del freq[s2[l]]
            l+=1
            freq[s2[i]]= freq.get(s2[i],0)+1
            if freq == target:
                return True
        return False