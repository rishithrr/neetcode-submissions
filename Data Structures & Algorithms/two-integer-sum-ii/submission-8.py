class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dt = {}
        for i, num in enumerate(numbers):
            if target - num in dt:
                return [dt[target-num], i+1]
            else:
                dt[num] = i+1