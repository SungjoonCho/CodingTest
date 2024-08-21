# LCS - 백준


# 풀이 참고함
# 2차원 DP 

import sys
from collections import deque


word1 = input()
word2 = input()

dp = [[0 for i in range(len(word2)+1)] for _ in range(len(word1)+1)]

# print(indexDict)

maxDPVal = 0
# for i in dp:
#     print(i)


for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        letter_i = i-1
        letter_j = j-1
        if word1[letter_i] == word2[letter_j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for i in dp:
#     print(i)

print(dp[-1][-1])

# print(calCnt)
