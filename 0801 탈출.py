
<<<<<<< HEAD
# 탈출 - 백준

=======
>>>>>>> f5fef32a6a0bc7dfbc4a043f13ff75fbc7a9c93a
from collections import deque

r,c = list(map(int, input().split()))

mat = []

dloc = []
sloc = []

water = deque()
visited = [[False for j in range(c)] for i in range(r)]

for i in range(r):
    mat.append(list(input()))
    
    for j in range(c):
        if(mat[i][j] == 'D'):
            dloc = [i,j]
        elif(mat[i][j] == 'S'):
            sloc = [i,j]
            mat[i][j] = '.'
        elif(mat[i][j] == '*'):
            water.append([i,j])
            visited[i][j] = True

# print(mat)
# print(water)

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

def in_range(y,x):
    return 0<=y and y<r and 0<=x and x<c

def water_bfs():
    global water, visited
    
    curCnt = len(water)
    if(curCnt == 0):
        return
    
    for i in range(curCnt):
        cy,cx = water.popleft()
        
        for dy, dx in zip(dys, dxs):
            ny,nx = cy+dy, cx+dx
            
            if (not in_range(ny,nx) or visited[ny][nx] == True or mat[ny][nx] == 'X' or mat[ny][nx] == 'D'):
                continue
            
            water.append([ny,nx])
            visited[ny][nx] = True
            mat[ny][nx] = '*'


def goseum_bfs(nextList):    
    
    g_queue = deque()
    g_visited = [[False for j in range(c)] for i in range(r)]
    bfsMat = [[0 for j in range(c)] for i in range(r)]
    
    for sloc in nextList:
        g_queue.append([sloc[:]])
        g_visited[sloc[0]][sloc[1]] = True    
    
    candList = []
    
    while(g_queue):
        curList = g_queue.popleft()
        cy,cx = curList[-1]
        
        # D이면 리턴
        if([cy,cx] == dloc):       
            
            candList.append(curList[1][:])
            continue
        
        for dy, dx in zip(dys, dxs):
            ny,nx = cy+dy, cx+dx
            
            if (not in_range(ny,nx) or g_visited[ny][nx] == True or mat[ny][nx] == 'X' or mat[ny][nx] == '*'):
                continue
                        
            if([ny,nx] != dloc):
                g_queue.append(curList + [[ny,nx]])
                g_visited[ny][nx] = True
                bfsMat[ny][nx] = bfsMat[cy][cx] + 1
            else:
                g_queue.append(curList + [[ny,nx]])
                
    
    # for i in bfsMat:
    #     print(i)
    # print()
    
    return candList  
    



# 물 한번 이동, 고슴도치 한번 이동 하는 방식으로 진행
# 물 이동 : 최근에 움직인 물만 이동
# 고슴도치 이동 : 가능한 루트가 여러가지일 수 있음. 그래서 가능한 path 중 목적지 도달 가능한 path만 추리고
# 해당 path에서 현재위치의 다음 pose들을 추림.
# 그리고 추려진 pose들을 이용해 다음번에 bfs 또 진행


candList = [sloc[:]]

t=0
while True:    
    t += 1
    
    # 물 이동 (D, X는 못감)
    water_bfs()
    
    # for i in mat:
    #     print(i)
    # print()
    
    # 고슴도치 이동 (현재 위치에서 물을 피해서 D까지 bfs)
    candList = goseum_bfs(candList[:])
    # print(candList)
    
    if(dloc in candList):
        print(t)
        exit()
        
    if(len(candList) == 0):
        print("KAKTUS")
        exit()
    
    