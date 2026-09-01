class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        target = {}
        for x in t:
            target[x] = target.get(x,0)+1
        l = 0
        result = ""
        form = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            if s[r] in target and freq[s[r]] == target[s[r]]:
                form+=1
            while form == len(target):
                le = r - l + 1
                if len(result) == 0 or le < len(result):
                    result = s[l:r + 1]
                freq[s[l]]-=1
                if s[l] in target and freq[s[l]] < target[s[l]]:
                    form-=1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l+=1
        return result