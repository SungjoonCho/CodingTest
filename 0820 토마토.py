
# 토마토 - 백준 

# bfs로 해결 , 큐의 각 요소가 며칠째에 익은 토마토인지 기록 필요

import sys
from collections import deque


def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<m


m, n = list(map(int, sys.stdin.readline().split()))

mat = [[0 for i in range(m)] for j in range(n)]
noFin = 0

queue = deque()
visited = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    mat[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if mat[i][j] == 0:
            noFin += 1
        elif mat[i][j] == 1:
            queue.append([i,j,0])
            visited[i][j] = True


if noFin == 0:
    print(0)
    exit(0)
    
    
    
cntDays = 0

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

while queue:
    
    cy,cx,cd = queue.popleft()
    cntDays = max(cntDays, cd)
    
    for dy, dx in zip(dys, dxs):
        ny, nx = cy+dy, cx+dx
        if not in_range(ny,nx) or visited[ny][nx] == True or mat[ny][nx] == 1 or mat[ny][nx] == -1:
            continue
        
        mat[ny][nx] = 1
        queue.append([ny,nx, cd+1])
        visited[ny][nx] = True
        noFin -= 1
        
        
        
if noFin == 0:
    print(cntDays)
else:
    print(-1)
    
