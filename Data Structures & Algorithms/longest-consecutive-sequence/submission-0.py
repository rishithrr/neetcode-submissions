class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        test=set(nums)

        max=0
        for num in nums:
            count=0
            n=num
            while(n in test):
                n-=1
                count+=1
            if count>max:
                max=count
        return max