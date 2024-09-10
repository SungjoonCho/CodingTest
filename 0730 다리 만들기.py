# 다리 만들기 (백준)
# https://www.acmicpc.net/problem/2146

# bfs로 각 나라마다 번호 매김, 각 나라의 경계선 구하기
# 각 경계에서 bfs로 다른 나라까지의 길이 구하기


n = int(input())
mat = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    mat[i] = list(map(int, input().split()))



gmat = [[0 for j in range(n)] for i in range(n)] # 나라 번호 표시
visited = [[False for j in range(n)] for i in range(n)] 
boundary = [] # (2차원 리스트)로 나라 번호 표시
boundaryMat = [[0 for j in range(n)] for i in range(n)] # 경계에 나라 번호 표시

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

gCnt = 1 # 나라 번호

def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<n

# 다른 나라 땅끼리는 무조건 바다로 분리되어있음
def groundNum(start):
    global gmat, gCnt, boundary, boundaryMat, visited
    
    # 바다이거나 이미 방문했으면 리턴
    if(mat[start[0]][start[1]] == 0 or visited[start[0]][start[1]] == True):
        return        
        
    queue = [start]
    
    visited[start[0]][start[1]] = True
    gmat[start[0]][start[1]] = gCnt
    tem_boundary = []
    
    while(queue):
        
        cy,cx = queue.pop(0)        
        for dy, dx in zip(dys, dxs):
            ny, nx = cy+dy, cx+dx
            
            if(not in_range(ny,nx) or visited[ny][nx] == True):
                continue
            elif(mat[ny][nx] == 0): 
                if boundaryMat[cy][cx] == 0:
                    tem_boundary.append([cy,cx])
                    boundaryMat[cy][cx] = gCnt
                continue            
            
            visited[ny][nx] = True
            gmat[ny][nx] = gCnt
            queue.append([ny,nx])            
    
    gCnt += 1
    boundary.append(tem_boundary)
                


def bfs_interCountry(start):
    
    bfsMat = [[0 for j in range(n)] for i in range(n)] 
    
    visited = [[False for j in range(n)] for i in range(n)] 
    queue = []
    
    queue.append([start[0],start[1]])
    visited[start[0]][start[1]] = True
    
    while(queue):
        cy,cx = queue.pop(0)        
        for dy, dx in zip(dys, dxs):
            ny, nx = cy+dy, cx+dx
            
            if(not in_range(ny,nx) or visited[ny][nx] == True):
                continue            
            elif(mat[ny][nx] != 0):
                
                # 땅이면서 && 현재 본인 땅과는 다른 숫자일 때
                if(boundaryMat[ny][nx] > 0 and boundaryMat[ny][nx] != boundaryMat[start[0]][start[1]]):
                    # for r in range(n):
                    #     print(bfsMat[r])
                    # print(bfsMat[cy][cx])
                    # print()
                    return bfsMat[cy][cx]
                
                continue
            
            visited[ny][nx] = True
            queue.append([ny,nx])    
            bfsMat[ny][nx] = bfsMat[cy][cx] + 1 
    
    return 1000000
    

# 섬마다 숫자 매기기, 각 섬의 해안가를 리스트에 담기
for r in range(n):
    for c in range(n):
        groundNum([r,c])



# 각 경계 지점마다 다른 나라까지의 최단 거리 구하기 
minCnt = 1000000
for i in boundary:
    for each in i:
        val = bfs_interCountry(each)
        minCnt = min(minCnt, val)

print(minCnt)

# for r in range(n):
#     print(bfsMat[r])

# for i in boundary:
#     print(len(i))


