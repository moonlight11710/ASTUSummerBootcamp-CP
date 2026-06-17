class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum = sum(nums[:k])
        maxsum = windowsum
        
        for i in range(len(nums)-k):
            windowsum = windowsum - nums[i] + nums[i+k]
            maxsum = max(windowsum, maxsum)
        return maxsum/k
            
