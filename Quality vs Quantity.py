t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split())) 
    lis.sort()
    red_sum = lis[0] + lis[1]
    blue_sum = lis[-1]
    left = 2
    right = n - 2
    possible = False
    if red_sum < blue_sum:
        possible = True
    while left < right:
        if red_sum < blue_sum:
            possible = True
            break
        red_sum += lis[left]
        blue_sum += lis[right]
        left += 1
        right -= 1
    if red_sum < blue_sum:
        possible = True
        
    if possible:
        print("YES")
    else:
        print("NO")
