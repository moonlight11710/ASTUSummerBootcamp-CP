t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    height = lis[0]
    prefixsum = [0]*n
    prefixsum[0] = lis[0]

    ans = []
    
    for i in range(1,n):
        prefixsum[i] = lis[i]+prefixsum[i-1]
        
    for i in range(n):
        height = min(height, (prefixsum[i]//(i+1)))
        ans.append(height)

    print(*ans)
    
