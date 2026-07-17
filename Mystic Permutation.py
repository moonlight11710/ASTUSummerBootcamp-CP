import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue
    check = sorted(lis)
    ans = []
    for i in range(n - 1):
        if check[0] == lis[i]:
            ans.append(check[1])
            check.pop(1)
        else:
            ans.append(check[0])
            check.pop(0)

    ans.append(check[0])

    if ans[-1] == lis[-1]:
        ans[-1], ans[-2] = ans[-2], ans[-1]
    print(*ans)
