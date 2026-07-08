t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    left = 0
    right = n -1 
    count = 0
    
    
    while left < right:
        if lis[left] == 0:
            left += 1
        elif lis[right] == 1:
            right -= 1
        else:
            count += 1
            left += 1
            right -= 1
    print(count)
    
