class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for c in s:
            if not c.isalnum():
                s=s.replace(c, "")
        mid = int((len(s)+1)/2)
        for i in range(1, mid+1):
            if s[i-1]!=s[-i]:
                return False
        return True

            
        