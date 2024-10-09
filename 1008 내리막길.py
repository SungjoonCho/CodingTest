# 내리막길 - 2번쨰
# https://www.acmicpc.net/problem/1520

import sys

def in_range(y,x):
    return 0<=y and y<H and 0<=x and x<W

def dfs(cy,cx):
    global dp

    if cy == H-1 and cx == W-1:
        return 1
    if dp[cy][cx] != -1:
        return dp[cy][cx]

    ways = 0
    for dy,dx in zip([0,-1,0,1],[1,0,-1,0]):
        ny, nx = cy+dy, cx+dx
        if in_range(ny,nx) == False:
            continue
        if mat[ny][nx] < mat[cy][cx]:
            ways += dfs(ny,nx)
    dp[cy][cx] = ways
    return dp[cy][cx]


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
H, W = map(int,input().split())
mat = []
for i in range(H):
    mat.append(list(map(int,input().split())))

dp = [[-1 for c in range(W)] for r in range(H)]
print(dfs(0,0))


# dp랑 dfs 함께 적용
# 이전에 이미 계산한 곳이라면 dp에 저장된 값을 읽어오기
