

# 치즈 - 백준
# https://www.acmicpc.net/problem/2638


# 구현, bfs

import sys
from collections import deque

def in_range(y,x):
    return 0<=y and y<N and 0<=x and x<M

input = sys.stdin.readline
N,M = list(map(int,input().split()))
mat = []
totalCheeze = 0
for i in range(N):
    mat.append(list(map(int,input().split())))
    for c in range(M):
        if mat[i][c] == 1:
            totalCheeze += 1

# 0,0에서부터 bfs 시작
# cntMat에 치즈 닿으면 각 pose에 1 추가, 만약 2가 되면 따로 리스트에 저장
# mat에 공기로 업데이트, totalCheeze에서 개수만큼 빼기
# totalCheeze 0 되면 끝

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

time = 0
while totalCheeze > 0:
    time += 1
    queue = deque()
    visited = [[False for i in range(M)] for j in range(N)]
    temCntMat = [[0 for i in range(M)] for j in range(N)]
    updateList = []

    queue.append([0,0])
    visited[0][0] = True
    while queue:
        cy, cx = queue.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = cy+dy, cx+dx
            if not in_range(ny,nx) or visited[ny][nx] == True:
                continue
            if mat[ny][nx] == 1:
                temCntMat[ny][nx] += 1
                if temCntMat[ny][nx] >= 2:
                    updateList.append([ny,nx])
            else:
                queue.append([ny,nx])
                visited[ny][nx] = True

    visited = [[False for i in range(M)] for j in range(N)]
    for cy,cx in updateList:
        if visited[cy][cx] == True:
            continue
        visited[cy][cx] = True
        totalCheeze -= 1
        mat[cy][cx] = 0

print(time)

