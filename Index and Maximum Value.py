t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lis = list(map(int, input().split()))
    _max = max(lis)
    res = []
    for i in range(m):
        op = list(input().split())
        
        if int(op[1]) <= _max <= int(op[2]):
            if op[0]=="+":
                _max+=1
            else:
                _max-=1
        res.append(_max)
    print(*res)
