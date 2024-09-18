
# 컨벤 데드가 하고싶어요 - 백준

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))
H = int(input())

dp = [[0 for i in range(M)] for j in range(N)]
dp[0][0] = mat[0][0]

if M > 1:
    for c in range(1,M):
        dp[0][c] = dp[0][c-1] + mat[0][c]
if N > 1:
    for r in range(1,N):
        dp[r][0] = dp[r-1][0] + mat[r][0]

for r in range(1,N):
    for c in range(1,M):
        dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + mat[r][c]

if dp[-1][-1] > H:
    print('NO')
else:
    print('YES')
    print(dp[-1][-1])


# DP 문제
# 2차원 DP - 각 DP 방 값은 위, 왼쪽의 값 중 최솟값 + 현재 헬창 눈치력 값으로 결정
