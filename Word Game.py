t = int(input())
for _ in range(t):
    n = int(input())

    a = set(map(str, input().split()))
    b = set(map(str, input().split()))
    c = set(map(str, input().split()))

    score_a = 0
    score_b = 0
    score_c = 0

    for i in a:
        if i in b and i in c:
            continue
        elif i in b or i in c:
            score_a += 1
        else:
            score_a +=3
    for i in b:
        if i in a and i in c:
            continue
        elif i in a or i in c:
            score_b += 1
        else:
            score_b +=3

    for i in c:
        if i in b and i in a:
            continue
        elif i in b or i in a:
            score_c += 1
        else:
            score_c +=3
            
            
    print(score_a, score_b, score_c)



    


