t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    balloon = 0
    seen = []
    for i in word:
        if i in seen:
            balloon+=1
        else:
            balloon+=2
            seen.append(i)
    print(balloon)
