t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    word1 = list(input().strip())
    word2 = list(input().strip())
    word1.sort()
    word2.sort()
    ans = []
    word1max = 0
    word2max = 0
   
    while word1 and word2:
        
        if word1[0] < word2[0]:
            word2max = 0
            if word1max == k:
                word1max = 0
                ans.append(word2[0])
                word2max += 1
                word2.pop(0)
            else:
                ans.append(word1[0])
                word1max += 1
                word1.pop(0)    
        else:
            word1max = 0
            if word2max == k:
                word2max = 0
                ans.append(word1[0])
                word1max += 1
                word1.pop(0)
            else:
                ans.append(word2[0])
                word2max += 1
                word2.pop(0)

    print(''.join(ans))
    
