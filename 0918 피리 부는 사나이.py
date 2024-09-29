
# 피리 부는 사나이 - 백준
# https://www.acmicpc.net/problem/16724

import sys

def in_range(y,x):
    return 0<=y and y<N and 0<=x and x<M

# 본인한테 온 경우가 있는지 확인 : 그런 케이스들은 visited True 처리 
def dfs_back(cy,cx):
    global visited

    for dy, dx in zip(dys,dxs):
        ny, nx = cy+dy, cx+dx
        if in_range(ny,nx) == False:
            continue
        d = direction[mat[ny][nx]]
        if ny + dys[d] == cy and nx + dxs[d] == cx and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs_back(ny,nx)

def dfs(cy,cx):
    global visited

    d = direction[mat[cy][cx]]
    dy, dx = dys[d], dxs[d]
    ny, nx = cy+dy, cx+dx
    if in_range(ny,nx) == True and visited[ny][nx] == False:
        visited[ny][nx] = True
        dfs(ny,nx)
        dfs_back(ny, nx)



sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(input().strip()))
visited = [[False for i in range(M)] for j in range(N)]

dys = [0,-1,0,1]
dxs = [1,0,-1,0]
direction = {'R':0, 'U':1, 'L':2, 'D':3}

answer = 0
for r in range(N):
    for c in range(M):
        if visited[r][c] == False:
            visited[r][c] = True
            dfs(r,c)
            dfs_back(r,c)
            answer += 1
print(answer)


# 분리 가능한 파트가 몇개인지 구하는 문제랑 똑같이 풀음

# 반복문으로 각 지점의 방문 여부 확인
# 방문 안했으면 재귀로 최대한 방문 가능한 모든 지점 체크
# 역방향으로도 체크 (자기한테 오는 화살표들 역으로 따라감)
# 그렇게 최대한 재귀 진행 후 분리 가능한 섬 개수 1 증가
