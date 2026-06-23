from math import ceil
t = int(input())
for _ in range(t):
    sum = 0
    n = int(input())
    lis = list(map(int, input().split()))
    
    print(ceil((max(lis)-min(lis))/2))
    
