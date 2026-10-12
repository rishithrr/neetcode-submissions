class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for i, v in enumerate(nums):
            if target - v not in dt:
                dt[v] = i
            else:
                return  [dt[target-v], i]