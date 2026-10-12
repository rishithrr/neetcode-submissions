class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    j+=1
                else:
                    sum=nums[i]+nums[j]
                    if target==sum:
                        return list((i,j))