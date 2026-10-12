class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums=set(nums)
        if len(nums)==1:
            return 1
        for num in nums:
            if num+1 not in nums and num-1 in nums:
                length=1
                while(num-1 in nums):
                    length+=1
                    num-=1
                res=max(res, length)
        return res
                

        