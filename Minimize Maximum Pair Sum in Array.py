class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        _max = 0
        
        while left<right:
            _max = max(_max,nums[left]+nums[right])
            right-=1
            left+=1
        return _max
