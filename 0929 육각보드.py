# 육각 보드 - 백준
# https://www.acmicpc.net/problem/12946

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dys, dxs = [-1,0,1,1,0,-1], [0,-1,-1,0,1,1]

def in_range(y,x):
    return 0<=y and y<N and 0<=x and x<N

def dfs(curPose, c):
    global answer, colorNum
    
    answer = max(1, answer)
    cy,cx = curPose[:]
    colorNum[cy][cx] = c

    for dy, dx in zip(dys, dxs):
        ny, nx = cy+dy, cx+dx
        if not in_range(ny,nx) or mat[ny][nx] == '-':
            continue

        if colorNum[ny][nx] == -1:
            answer = max(answer, 2)
            dfs([ny,nx], (c+1)%2)
        elif colorNum[ny][nx] == c:
            print(3)
            exit(0)



N = int(input())
mat = []
colorValid = set()
for i in range(N):
    mat.append(input().strip())
    for c in range(N):
        if mat[i][c] == 'X':
            colorValid.add((i,c))

answer = 0
colorNum = [[-1 for i in range(N)] for j in range(N)]
for eachPose in colorValid:
    if colorNum[eachPose[0]][eachPose[1]] == -1:
        dfs(eachPose, 0)

print(answer)

# bfs
# https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-12946%EB%B2%88-%EC%9C%A1%EA%B0%81%EB%B3%B4%EB%93%9C\

