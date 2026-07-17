t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    
    found = False
    for i in range(1, n - 1):
        if lis[i] > lis[i-1] and lis[i] > lis[i+1]:
            print("YES")
            print(i, i + 1, i + 2)
            found = True
            break
            
    if not found:
        print("NO")
