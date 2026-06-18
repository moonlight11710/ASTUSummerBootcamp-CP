class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        _sum = target[0]

        prev = target[0]

        for i in range(1,len(target)):
            if target[i]>prev:
                _sum+=target[i]-prev
            prev=target[i]
        return _sum

        
    
