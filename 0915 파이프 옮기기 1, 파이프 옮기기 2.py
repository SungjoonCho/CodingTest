

# 파이프 옮기기 1, 2 - 백준
# https://www.acmicpc.net/problem/17070
# https://www.acmicpc.net/problem/17069


# bfs로는 시간 초과
# dp로 해야 됨

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

drs = [0,1,1]
dcs = [1,1,0]

dp = [[[0,0,0] for i in range(N)] for j in range(N)]
dp[0][0][0] = 1
for i in range(1,N):
    if mat[0][i] == 1:
        break
    dp[0][i][0] = 1

for r in range(1,N):
    for c in range(2,N):
        if mat[r][c] == 1:
            continue

        # 노란색
        dp[r][c][0] = sum(dp[r][c - 1][:2])
        # 연두색
        dp[r][c][2] = sum(dp[r-1][c][1:])
        # 파란색
        if mat[r-1][c] == 0 and mat[r][c] == 0 and mat[r][c-1] == 0:
            dp[r][c][1] = sum(dp[r-1][c-1])

print(sum(dp[r][c]))
