
# 평범한 배낭
# https://www.acmicpc.net/problem/12865


import sys
input = sys.stdin.readline

N, K = map(int,input().split())
bagInfo = []
for i in range(N):
    bagInfo.append(list(map(int,input().split())))

dp = [[0 for i in range(K+1)] for j in range(N+1)]
for r in range(1,N+1):
    for c in range(1,K+1):
        w,v = bagInfo[r-1]
        if c-w < 0:
            dp[r][c] = dp[r-1][c]
            continue
        dp[r][c] = max(dp[r-1][c], dp[r-1][c-w] + v)

print(dp[-1][-1])


# 냅색 문제
# https://velog.io/@dmsgur7112/Knapsack%EB%B0%B0%EB%82%AD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
