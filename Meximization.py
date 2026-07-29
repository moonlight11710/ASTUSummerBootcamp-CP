t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    res=[]
    dup=[]
    set1=set()
    for i in range(n):
        if lis[i] not in set1:
            res.append(lis[i])
            set1.add(lis[i])
        else:
            dup.append(lis[i])
    ans= res+ dup
    print(*ans)
        




