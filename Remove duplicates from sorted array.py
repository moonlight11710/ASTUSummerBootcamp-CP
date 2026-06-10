class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        seen = []
        i=0
        while i < len(nums):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.append(nums[i])
                i+=1
        
