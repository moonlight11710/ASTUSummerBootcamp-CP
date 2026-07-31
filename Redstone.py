from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))

    dict = Counter(lis)

    for i in dict:
        if dict[i] >= 2:
            print("YES")
            break
    else:
        print("NO")



    

