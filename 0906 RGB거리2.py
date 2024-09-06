# RGB거리 2
# https://www.acmicpc.net/problem/17404

import sys

input = sys.stdin.readline
n = int(input())
colorInfo = []
for i in range(n):
    colorInfo.append(list(map(int, input().split())))

answer = 1e9
for i in range(3):
    dp = [[1e9,1e9,1e9] for j in range(n)]
    dp[0][i] = colorInfo[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + colorInfo[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + colorInfo[j][1]
        dp[j][2] = min(dp[j-1][1], dp[j-1][0]) + colorInfo[j][2]
    
    for k in range(3):
        if i != k: # 첫번째 색깔, n-1번째 색깔이 달라야됨
            answer = min(answer, dp[-1][k])

print(answer)
