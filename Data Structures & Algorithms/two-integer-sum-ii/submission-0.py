class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dt={}
        for i, val in enumerate(numbers):
            diff=target-val
            if diff in dt:
                return [dt[diff]+1, i+1]
            dt[val]=i
        