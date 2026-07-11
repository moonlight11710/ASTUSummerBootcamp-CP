t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    chairs = 0
    for i in range(n):
        if lis[i] <= (i + 1):
            chairs += 1  
    print(chairs)
