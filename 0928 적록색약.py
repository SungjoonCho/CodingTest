

# 적록색약

import sys
from collections import deque
input = sys.stdin.readline

def in_range(y,x):
    return 0<=y and y<N and 0<=x and x<N

def bfs_normal():
    visit = [[False for i in range(N)] for j in range(N)]
    queue = deque()
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visit[r][c] == True:
                continue

            cnt += 1
            visit[r][c] = True
            queue.append((r,c))
            while queue:
                cy,cx = queue.popleft()
                for dy, dx in zip(dys, dxs):
                    ny,nx = cy+dy, cx+dx
                    if in_range(ny,nx) == False or visit[ny][nx] == True:
                        continue
                    if mat[ny][nx] != mat[cy][cx]:
                        continue
                    visit[ny][nx] = True
                    queue.append((ny,nx))
    return cnt

def bfs_RedGreen():
    visit = [[False for i in range(N)] for j in range(N)]
    queue = deque()
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visit[r][c] == True:
                continue

            cnt += 1
            visit[r][c] = True
            queue.append((r,c))
            while queue:
                cy,cx = queue.popleft()
                for dy, dx in zip(dys, dxs):
                    ny,nx = cy+dy, cx+dx
                    if in_range(ny,nx) == False or visit[ny][nx] == True:
                        continue
                    if mat[ny][nx] != mat[cy][cx] and 'B' in [mat[ny][nx], mat[cy][cx]]:
                        continue
                    visit[ny][nx] = True
                    queue.append((ny,nx))
    return cnt

N = int(input())
mat = []
for i in range(N):
    mat.append(input())

dys = [0,-1,0,1]
dxs = [1,0,-1,0]
print(bfs_normal(), bfs_RedGreen())
