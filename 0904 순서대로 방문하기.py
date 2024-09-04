# 순서대로 방문하기 - 소프티어
# https://softeer.ai/practice/6246

import sys

def dfs(curPose, curCnt):
    global result, visited

    if curCnt == m-1:
        result += 1
        return      

    cy,cx = curPose[:]
    for dy,dx in zip(dys, dxs):
        ny,nx = cy+dy, cx+dx
        if (0<=ny and ny <n and 0<=nx and nx<n) == False or visited[ny][nx] == True or mat[ny][nx] == 1:
            continue

        if orderMat[ny][nx] != -1 and orderMat[ny][nx] != curCnt+1:
            continue

        visited[ny][nx] = True 
        if orderMat[ny][nx] == -1:     
            dfs([ny,nx], curCnt)
        elif orderMat[ny][nx] == curCnt+1:   
            dfs([ny,nx], curCnt+1)
        visited[ny][nx] = False           
            
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

visitPlan = []
orderMat = [[-1 for c in range(n)] for r in range(n)]
for i in range(m):
    y,x = list(map(int, input().split()))
    visitPlan.append([y-1,x-1])
    orderMat[y-1][x-1] = i    

dys = [0,-1,0,1]
dxs = [1,0,-1,0]
result = 0

visited = [[False for c in range(n)] for r in range(n)]
init_y, init_x = visitPlan[0][:]
visited[init_y][init_x] = True

dfs(visitPlan[0][:], 0)
print(result)
