t = int(input())

for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))


    left = lis.index(max(lis))
    right = lis.index(max(lis))

    possible = True
    for i in range(n-1,0,-1):
        if lis.index(i) == left - 1:
            left -= 1
        elif lis.index(i) == right + 1:
            right += 1
        else:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")

    

