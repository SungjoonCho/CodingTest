
# 로봇 - 백준
# https://www.acmicpc.net/problem/1726


# bfs 하되 데이터 관리를 3차원으로 해서 같은 위치여도 각 방향에 있어본 적이 있는지 체크


from collections import deque

m,n = list(map(int, input().split()))

mat = [[0 for i in range(n)]for j in range(m)]

for i in range(m):
    mat[i] = list(map(int, input().split()))
    
start = list(map(int, input().split()))
end = list(map(int, input().split()))

for i in range(len(start)):
    start[i] -= 1
    end[i] -= 1
    
# 방향은 동쪽이 0, 서쪽이 1, 남쪽이 2, 북쪽이 3


queue = deque()
visited = [[[False] * 4 for i in range(n)]for j in range(m)]
bfsMat = [[[0] * 4 for i in range(n)]for j in range(m)]

queue.append(start[:])
visited[start[0]][start[1]][start[2]] = True


def possible_nd(cd):
    if(cd == 0):    
        dys = [-1,1]
        dxs = [0,0]
        nds = [3,2]
    elif(cd == 1):    
        dys = [-1,1]
        dxs = [0,0]
        nds = [3,2]
    elif(cd == 2):    
        dys = [0,0]
        dxs = [-1,1]
        nds = [1,0]
    elif(cd == 3):    
        dys = [0,0]
        dxs = [-1,1]
        nds = [1,0]
        
    return dys, dxs, nds

def convert_cd(cd):
    if(cd == 0):    
        dir = [0,1]
    elif(cd == 1):    
        dir = [0,-1]
    elif(cd == 2):    
        dir = [1,0]
    elif(cd == 3):    
        dir = [-1,0]
        
    return dir

def in_range(y,x):
    return 0<= y and y<m and 0<=x and x<n



# 3차원 visited, bfsmat으로 풀음
# 이미 갔던 곳이라도 각 방향으로 가봤는지 체크해야 되고, 같은 위치에서 회전할 때에도 +1 해줘야됨

while(queue):
    curPose = queue.popleft()
    cy, cx, cd = curPose
    
    # print(curPose)
    # print(bfsMat[cy][cx][cd])
    
    if(curPose == end):
        print(bfsMat[cy][cx][cd])
        break
    
    # go k
    dir = convert_cd(cd)
    for amount in range(1,4):
        ny,nx = cy + dir[0] * amount , cx + dir[1] * amount
        
        
        # 어차피 더 이상 갈 수 없음
        if(not in_range(ny,nx) or mat[ny][nx] == 1):
            break
        
        if(visited[ny][nx][cd]):
            continue
        
        
        queue.append([ny,nx,cd])  
        visited[ny][nx][cd] = True              
        bfsMat[ny][nx][cd] = bfsMat[cy][cx][cd] + 1 # 다음 위치, 현재 방향에 + 1
        # print(ny,nx,cd)
    
    # turn dir
    dys, dxs, nds = possible_nd(cd)        
    for nd in nds:
                
        if(visited[cy][cx][nd]):
            continue
        
        queue.append([cy,cx,nd])
        bfsMat[cy][cx][nd] = bfsMat[cy][cx][cd] + 1 # 현재 위치, 다음 방향에 +1
        visited[cy][cx][nd] = True
        # print(cy,cx,nd)
        

# print()
# for i in range(m):
#     print(bfsMat[i])
    
# for i in range(m):
#     print(visited[i])
