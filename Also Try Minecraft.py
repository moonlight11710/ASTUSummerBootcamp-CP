n, m = map(int, input().split())
lis = list(map(int, input().split()))

forward = [0] * n
for i in range(1, n):
    curr = max(0, lis[i-1] - lis[i])
    forward[i] = forward[i-1] + curr


backward = [0] * n
for i in range(n-2, -1, -1):
    step_damage = max(0, lis[i+1] - lis[i])
    backward[i] = backward[i+1] + step_damage

for _ in range(m):
    s, j = map(int, input().split())
    s2 = s - 1
    j2 = j - 1

    if s2 < j2:
        print(forward[j2] - forward[s2])
    else:
        print(backward[j2] - backward[s2])
