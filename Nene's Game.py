t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    ans = []
    for i in range(q):
        ans.append(min(a1[0]-1,a2[i]))
    print(*ans)
