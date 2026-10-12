class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt={}
        for i, val in enumerate(nums):
            if target - val not in dt:
                dt[val]=i
            else:
                return sorted([i, dt[target - val]])
        return []