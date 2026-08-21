class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans+=str(len(s))
            ans+="#"
            ans+=s
        return ans
    def decode(self, s: str) -> List[str]:
        result = []
        num =""

        i = 0
        while i < len(s):
            if s[i] == '#':
                n = int(num)
                word = s[i+1:i+n+1]
                result.append(word)
                i+=n+1
                num =""
            else:
                num+=s[i]
                i+=1
        return result
            