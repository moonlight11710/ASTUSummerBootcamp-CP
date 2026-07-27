n = int(input())
lis = input()
ans = ["0"]*10
for i in range(n):
    if lis[i] == "L":
        idx = 0
        for j in range(10):
            if ans[j] == "0":
                idx = j
                break
        ans[idx] = "1"
    elif lis[i] == "R":
        idx = 0
        for j in range(9,-1,-1):
            if ans[j] == "0":
                idx = j
                break
        ans[idx] = "1"
    else:
        ans[int(lis[i])] = "0"
print("".join(ans))
