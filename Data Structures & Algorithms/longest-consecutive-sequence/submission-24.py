class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        largest = 0
        for num in nums:
            if num-1 not in nums:
                longest = 1
                while num+longest in nums:
                    longest+=1
                largest = max(longest, largest)
        return largest