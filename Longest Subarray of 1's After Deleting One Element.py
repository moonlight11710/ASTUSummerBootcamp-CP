class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        _max = 0
        if nums.count(0)==0:
            return len(nums)-1

        window = defaultdict(int)
        
        left = 0
        for right in range(len(nums)):
            window[nums[right]]+=1
            while window[0]>1:
                window[nums[left]]-=1
                left+=1
            _max = max(_max,window[1])
        
        return _max
            
             

