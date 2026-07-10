t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    lis = list(map(int, input().split()))
    possible  = True
    
    pref = [0] * (n + 1)
    totalsum = sum(lis)
    for i in range(n):
        pref[i+1] = pref[i] + lis[i]

    for i in range(q):
        l,r,k = list(map(int, input().split()))
        if (totalsum - pref[r] + pref[l-1] + k*(r-l+1)) % 2 != 0:
            print("YES")
        else:
            print("NO")
