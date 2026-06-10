class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        st = "".join(str(x) for x in nums)
        return st.count(str(digit))
