# 연구소 = 백준


from collections import deque


# dfs로 벽 3개 가정하고
# 각 케이스에 대해 bfs로 바이러스 확산

n, m = list(map(int, input().split())) # 세로, 가로
mat = [[0 for i in range(m)] for j in range(n)]

virusPose = deque()
wallPose = deque()
blankPose = deque()

for r in range(n):
    mat[r] = list(map(int, input().split()))
    for c in range(m):
        if mat[r][c] == 2:
            virusPose.append([r,c])
        elif mat[r][c] == 1:
            wallPose.append([r,c])
        else:
            blankPose.append([r,c])
            


used = [False for _ in range(len(blankPose))]
curWallCnt = 0
maxSafe = 0

def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<m
    
def virusDiffusion():
    global maxSafe
    
    curSafe = len(blankPose)-3
    dys = [0,-1,0,1]
    dxs = [1,0,-1,0]
    
    virusPose_tem = virusPose.copy()
    visited = [[False for i in range(m)] for j in range(n)]
    
    while virusPose_tem:
        curPose = virusPose_tem.popleft()
        cy,cx = curPose
        
        for dy,dx in zip(dys, dxs):
            ny,nx = cy+dy, cx+dx
            if not in_range(ny,nx) or visited[ny][nx] == True or mat[ny][nx] != 0:
                continue
            
            virusPose_tem.append([ny,nx])
            visited[ny][nx] = True
            curSafe -= 1
    
    maxSafe = max(maxSafe, curSafe)
        
    

def dfs(idx):
    global curWallCnt, used
    
    if curWallCnt == 3:
        # 바이러스 확산 시뮬레이션, 개수 세기, 업데이트
        virusDiffusion()        
        return    
    
    for i in range(idx, len(blankPose)):
        if(used[i] == False):
            used[i] = True
            curWallCnt += 1
            # 벽 세우기
            cr,cc = blankPose[i]
            mat[cr][cc] = 1            
            
            dfs(i+1) #idx+1 주면 안되고 i+1 줘야됨 (그래야 최소 i 다음꺼부터 확인하고 벽을 추가하니까)
            
            used[i] = False
            curWallCnt -= 1
            mat[cr][cc] = 0
            
            
dfs(0)
print(maxSafe)
