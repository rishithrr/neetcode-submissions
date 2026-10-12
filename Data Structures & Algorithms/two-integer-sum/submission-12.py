class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for i, num in enumerate(nums):
            if target - num in dt:
                return [dt[target - num], i]
            else:
                dt[num] = i