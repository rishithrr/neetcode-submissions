class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = []
        prefix = 1
        for num in nums:
            p.append(prefix)
            prefix *=num

        s = []
        suffix = 1
        for num in nums[::-1]:
            s.append(suffix)
            suffix *= num
        s = [i for i in s[::-1]]
        
        res = []
        for i in range(len(nums)):
            res.append(p[i]*s[i])
        return res