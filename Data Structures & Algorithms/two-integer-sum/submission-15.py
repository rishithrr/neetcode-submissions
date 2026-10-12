class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for i, v in enumerate(nums):
            if target - v in dt:
                return [dt[target-v], i]
            dt[v] = i