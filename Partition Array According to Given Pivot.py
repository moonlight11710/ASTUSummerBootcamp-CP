class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        middle = []
        higher = []
        for i in nums:
            if i>pivot:
                higher.append(i)
            elif i<pivot:
                lower.append(i)
            else:
                middle.append(i)
        return lower+middle+higher
