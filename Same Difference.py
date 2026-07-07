t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    a = word.count(word[-1])
    print(n-a)

