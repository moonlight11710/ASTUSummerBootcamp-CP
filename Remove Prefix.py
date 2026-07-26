t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    seen = set()
    lis.reverse()


    for i in range(n):
        if lis[i] in seen:
            print(n-i)
            break
        else:
            seen.add(lis[i])
    else:
        print(0)




