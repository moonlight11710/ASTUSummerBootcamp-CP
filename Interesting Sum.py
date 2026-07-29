t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    print((lis[-1]-lis[0])+(lis[-2]-lis[1]))
