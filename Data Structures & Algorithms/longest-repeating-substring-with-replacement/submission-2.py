class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0 
        cnt = 0
        maxfreq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            maxfreq = max(maxfreq,freq[s[r]])
            while r - l + 1 > maxfreq + k:
                freq[s[l]]-=1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l+=1
            cnt = max(cnt,r-l+1)
        return cnt