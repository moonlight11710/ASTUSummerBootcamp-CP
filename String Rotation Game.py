t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    count = 1
    same= 0
    for i in range(n-1):
        if word[i]!= word[i+1]:
            count += 1
        else:
            same += 1
    
    if word[0] == word[-1] or same == 0:
        print(count)
    else:
        print(count + 1)
