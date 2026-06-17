class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue
            length = 1
            j = i + 1
            while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2 :
                length += 1
                j += 1
            ans = max(ans, length)

        return ans
