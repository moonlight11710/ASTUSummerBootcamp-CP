n, q = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort(reverse = True)
pref = [0]*(n+1)
pref[1]= lis[0]
for i in range(n):
    pref[i+1] = lis[i] + pref[i]

for _ in range(q):
    x, y = map(int, input().split())
    new = pref[x]-pref[x-y]
    print(new)
    


