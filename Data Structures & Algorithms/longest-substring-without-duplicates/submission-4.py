class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        n = len(s)
        l = 0
        dist= 0 
        for r in range(n):
            freq[s[r]] = freq.get(s[r],0)+1
            while freq[s[r]] > 1:
                freq[s[l]]-=1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l+=1
            dist = max(dist,r - l + 1)
        return dist