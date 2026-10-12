class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not set(nums):
            return 0
        nums=set(nums)
        max_count=1
        for num in nums:
            count=0
            if num+1 not in nums and num-1 in nums:
                count+=1
                while(num-1 in nums):
                    count+=1
                    num=num-1
                max_count=max(max_count, count)
            else:
                count=1
                max_count=max(max_count, count)
        return max_count