class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_str = ''
        for c in s:
            if c.isalnum():
                f_str+=c.lower() 
        return f_str == f_str[::-1]