class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(n):
            r = (i+2)%n
            m = (i+1)%n
            if colors[i] == colors[r] and colors[i] != colors[m]:
                ans += 1
            
        return ans
