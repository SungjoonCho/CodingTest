
# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

def in_range(y,x):
    return 0<=y and y<N and 0<=x and x<N

def bfs(cy,cx):
    global cnt
    queue = deque()
    queue.append((cy,cx))
    visited[cy][cx] = True

    while queue:
        cy,cx = queue.popleft()
        cnt += 1
        for dy,dx in zip(dys,dxs):
            ny,nx = cy+dy, cx+dx
            if not in_range(ny,nx) or visited[ny][nx] == True or mat[ny][nx] == '0':
                continue
            queue.append((ny,nx))
            visited[ny][nx] = True

N = int(input())
mat = []
for i in range(N):
    mat.append(input().strip())
visited = [[False for i in range(N)] for j in range(N)]
dys,dxs = [0,-1,0,1], [1,0,-1,0]

answer = []
for r in range(N):
    for c in range(N):
        if mat[r][c] == '0' or visited[r][c] == True:
            continue
        cnt = 0
        bfs(r,c)
        answer.append(cnt)
      
answer.sort()
print(len(answer))
for i in answer:
    print(i)
