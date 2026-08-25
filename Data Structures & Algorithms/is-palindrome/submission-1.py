class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for x in s:
            if x.isalnum():
                a+=x.lower()
        l = 0
        r = len(a) -1 
        while l < r:
            if a[l] != a[r]:
                return False
            l+=1
            r-=1
        return True