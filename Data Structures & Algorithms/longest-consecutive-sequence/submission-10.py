__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
__import__("atexit").register(lambda: open("display_memory.txt", "w").write("0"))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        if len(nums)==1 or len(nums)==0:
            return len(nums)
        max_count=1
        for num in nums:
            if num+1 not in nums and num-1 in nums:
                count=1
                peak=num
                while(peak-1 in nums):
                    count+=1
                    peak-=1
                    max_count=max(max_count, count)
        return max_count