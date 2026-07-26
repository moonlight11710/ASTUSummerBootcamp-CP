t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    capacity = list(map(int, input().split()))
    initial = list(map(int, input().split()))
    current = []
    ans = []

    for i in range(n):
        current.append([initial[i],i+1])

    current.sort(reverse = True)

    for level, index in current:
        while level < k+1:
            ans.append(index)
            level+=1
    print(len(ans))
    print(*ans)
    





    
