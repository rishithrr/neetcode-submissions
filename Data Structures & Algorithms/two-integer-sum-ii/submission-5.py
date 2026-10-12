class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dt = {}
        for i, v in enumerate(numbers):
            if target - v in dt:
                return [dt[target - v] + 1, i + 1]
            else:
                dt[v] = i