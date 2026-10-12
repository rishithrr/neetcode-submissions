class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        test=set(nums)

        max=0
        for num in nums:
            count=1
            if num+1 not in test:

                while(num-1 in test):
                    num-=1
                    count+=1
            if count>max:
                max=count
        return max