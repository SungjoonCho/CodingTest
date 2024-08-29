
# 마법의 숲 - 코드트리 (삼성 기출)
# https://www.codetree.ai/training-field/frequent-problems/problems/magical-forest-exploration/description?page=1&pageSize=5



def in_range(y,x):
    return 0<=y and y<R and 0<=x and x<C

def in_range_colli_down(y,x): # next y, next x가 옴
    
    check1_y, check1_x = y+1, x
    check2_y, check2_x = y, x-1
    check3_y, check3_x = y, x+1
    
    if y == -1: # 아래만 체크        
        # range 체크, 충돌 체크
        if not in_range(check1_y, check1_x) or mat[check1_y][check1_x] != 0:
            return False
        
    else: # 아래, 아래좌우 체크        
        if not in_range(check1_y, check1_x) or mat[check1_y][check1_x] != 0:
            return False
        if not in_range(check2_y, check2_x) or mat[check2_y][check2_x] != 0:
            return False
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        
    return True
        
    
def in_range_colli_rotWest(y,x):
    
    check1_y, check1_x = y-1, x
    check2_y, check2_x = y, x-1
    check3_y, check3_x = y+1, x
    check4_y, check4_x = y+1, x-1
    check5_y, check5_x = y+2, x    
    
    if y==-2:
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
        
    elif y == -1: 
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        if not in_range(check4_y, check4_x) or mat[check4_y][check4_x] != 0:
            return False
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
        
    elif y == 0:
        if not in_range(check2_y, check2_x) or mat[check2_y][check2_x] != 0:
            return False
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        if not in_range(check4_y, check4_x) or mat[check4_y][check4_x] != 0:
            return False
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
    
    else:
        if not in_range(check1_y, check1_x) or mat[check1_y][check1_x] != 0:
            return False
        if not in_range(check2_y, check2_x) or mat[check2_y][check2_x] != 0:
            return False
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        if not in_range(check4_y, check4_x) or mat[check4_y][check4_x] != 0:
            return False
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
    
    return True

def in_range_colli_rotEast(y,x):
    
    check1_y, check1_x = y-1, x
    check2_y, check2_x = y, x+1
    check3_y, check3_x = y+1, x
    check4_y, check4_x = y+1, x+1
    check5_y, check5_x = y+2, x    
    
    if y==-2:
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
        
    elif y == -1: 
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        if not in_range(check4_y, check4_x) or mat[check4_y][check4_x] != 0:
            return False
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
        
    elif y == 0:
        if not in_range(check2_y, check2_x) or mat[check2_y][check2_x] != 0:
            return False
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        if not in_range(check4_y, check4_x) or mat[check4_y][check4_x] != 0:
            return False
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
    
    else:
        if not in_range(check1_y, check1_x) or mat[check1_y][check1_x] != 0:
            return False
        if not in_range(check2_y, check2_x) or mat[check2_y][check2_x] != 0:
            return False
        if not in_range(check3_y, check3_x) or mat[check3_y][check3_x] != 0:
            return False
        if not in_range(check4_y, check4_x) or mat[check4_y][check4_x] != 0:
            return False
        if not in_range(check5_y, check5_x) or mat[check5_y][check5_x] != 0:
            return False
        
    return True

def draw(y,x, i):
    mat[y][x] = i
    for dy, dx in zip(dys, dxs):
        ny,nx = y+dy, x+dx
        # print(ny, nx)
        mat[ny][nx] = i
    
    
def bfs(cy,cx, num):
    # print(num)
    
    queue = []
    visited = [[False for i in range(C)] for j in range(R)]
    mostLowRow = 0
    
    queue.append([cy,cx, num])
    visited[cy][cx] = True
    
    while queue:
        cy,cx, curNum = queue.pop(0)
        
        for dy, dx in zip(dys,dxs):
            ny, nx = cy+dy, cx+dx
            if not in_range(ny,nx) or mat[ny][nx] == 0 or visited[ny][nx] == True:
                continue
            
            # 숫자 같으면 갈 수 있음 or 다른 골렘으로 넘어가기
            if mat[ny][nx]==curNum or (mat[ny][nx] != curNum and exitMat[cy][cx] == curNum):
                queue.append([ny,nx, mat[ny][nx]])
                visited[ny][nx] = True
                mostLowRow = max(mostLowRow, ny)
    
    # print('bfs')
    # for i in visited:
    #     print(i)
    # print('bfs', mostLowRow+1)
    # print()
    
    return mostLowRow+1
            
            
            
            

R, C, K = list(map(int, input().split()))

mat = [[0 for i in range(C)] for j in range(R)]
exitMat = [[0 for i in range(C)] for j in range(R)]


gollem_info = []
for i in range(K):
    c, direction = list(map(int, input().split()))
    gollem_info.append([c-1, direction])
    
# print(gollem_info)


dys = [-1,0,1,0]
dxs = [0,1,0,-1]


totalScore = 0
for idx, eachGollem in enumerate(gollem_info):
    
    # 각 골렘 넘버 매김 (1부터 시작)
    golNum = idx+1
    
    # print(golNum)
    # for i in mat:
    #     print(i)
    # print()
    # for i in exitMat:
    #     print(i)
    # print()
    
    
    # center만 가지고 다니기 (갈 곳 체크할때 범위만 보면 되니까)
    cur_x, direction = eachGollem
    cur_y = -2
    
    # 이동
    while True:
        # print('gollemPose', cur_y, cur_x, direction)
    
        # 내려갈 곳 계산
        next_y, next_x = cur_y+1, cur_x
        # in_range_down 체크
            # True면 실제 이동 후 continue      
        if in_range_colli_down(next_y, next_x) == True:
            cur_y, cur_x = next_y, next_x             
            continue
        
        next_y, next_x = cur_y, cur_x-1        
        # in_range_colli_rotWest 체크
            # True면 실제 이동 후 continue
        if in_range_colli_rotWest(next_y, next_x) == True:
            cur_y, cur_x = next_y+1, next_x 
            direction -= 1
            if direction == -1:
                direction = 3
            continue
        
        
        next_y, next_x = cur_y, cur_x+1 
        # in_range_colli_rotEast 체크
            # True면 실제 이동 후 continue
        if in_range_colli_rotEast(next_y, next_x) == True:
            cur_y, cur_x = next_y+1, next_x 
            direction += 1
            if direction == 4:
                direction = 0
            continue
        
        break 
    

    
    
    # 만약 골렘 일부가 밖에 있으면 mat, exitMat 초기화
    # cur_y <= 0로 판단하면 될듯
    if cur_y <= 0:
        mat = [[0 for i in range(C)] for j in range(R)]
        exitMat = [[0 for i in range(C)] for j in range(R)]
        continue
    
    # print('gollemPose', cur_y, cur_x, direction)
    # mat에 그리기 (현재 골렘 인덱스 넘버로 채우기) , 각 골렘의 입구는 따로 mat 만들어서 저장
    draw(cur_y, cur_x, golNum)
    exitMat[cur_y+dys[direction]][cur_x+dxs[direction]] = golNum
        

    
    # 정령 하강 & 점수 획득
    totalScore += bfs(cur_y, cur_x, golNum)
    
print(totalScore)
