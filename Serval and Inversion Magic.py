t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    left = 0
    right = n - 1 
    state = 0 
    possible = True
    while left < right:
        if s[left] != s[right]:
            if state == 0:
                state = 1 
            elif state == 2:
                possible = False
                break
        else:
            if state == 1:
                state = 2

        left += 1
        right -= 1

    if possible:
        print("YES")
    else:
        print("NO")
