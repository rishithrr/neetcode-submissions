class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        if len(nums)==1:
            return 1
        nums=list(nums)
        
        max_count=0
        for i in range(len(nums)):
            if nums[i]+1 not in nums and nums[i]-1 in nums:
                count=0
                peak=nums[i]
                while(peak-1 in nums):
                    count+=1
                    peak-=1
                count+=1
                if count>max_count:
                    max_count=count
        return max_count