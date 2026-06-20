class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        sum = 0
        left = 0
        
        for right in range(len(prices)-1):
            if prices[right]-prices[right+1]==1:
                continue
            n = right-left+1
            print(left,right)
            print(n)
            sum+=n*(n+1)//2
            print(sum)
            left = right+1
        n = len(prices) - left
        sum+=n*(n+1)//2
        if sum == len(prices) - 1:
            return len(prices)
        return sum
