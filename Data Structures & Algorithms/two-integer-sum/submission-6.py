class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in dt:
                return [dt[diff], i]
            dt[n]=i
        