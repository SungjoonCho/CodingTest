
# 내리막길 1520 - 백준

# https://studyandwrite.tistory.com/387 참고함

# DFS + DP
# 각 지점에서 도착지까지의 경로 개수를 저장해놓고
# 만약 기존 저장된 곳을 재방문한다면 거기에 저장된 값 그대로 사용



import sys
from collections import deque




m ,n = list(map(int, input().split())) # 세로 가로

mat = [[0 for i in range(n)] for j in range(m)]
dp = [[-1 for i in range(n)] for j in range(m)]


for i in range(m):
    mat[i] = list(map(int, sys.stdin.readline().split()))


dys = [0 ,-1 ,0 ,1]
dxs = [1 ,0 ,-1 ,0]

def in_range(y ,x):
    return 0<= y and y < m and 0 <= x and x < n


def dfs(cy, cx):

    if cy == m - 1 and cx == n - 1:
        return 1

    if dp[cy][cx] != -1: # 0이기라도 하면 리턴(가봤다는거니까)
        return dp[cy][cx]

    ways = 0
    for dy, dx in zip(dys, dxs):
        ny, nx = cy + dy, cx + dx

        if not in_range(ny, nx):
            continue

        if mat[ny][nx] < mat[cy][cx]:
            ways += dfs(ny, nx) ### 해당 지점에서의 갈래길에서 갈 수 있는 경우의 수 누적

    dp[cy][cx] = ways
    return dp[cy][cx]


answer = dfs(0, 0)
print(answer)
