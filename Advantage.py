t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    _max = max(lis)
    lis2 = lis[:]
    lis2.pop(lis2.index(_max))
    second = max(lis2)
    
    ans = []
    for i in range(n):
        if lis[i]==_max:
            ans.append(lis[i]-second)
        else:
            ans.append(lis[i]-_max)
    print(*ans)
   
