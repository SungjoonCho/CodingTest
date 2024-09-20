
# 술래잡기 - 코드트리
# https://www.codetree.ai/training-field/frequent-problems/problems/hide-and-seek/description?page=4&pageSize=5

def distBtwSoole(y,x):
    return abs(y-soolePose[0]) + abs(x-soolePose[1])

def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<n

def moveDomang():
    global peopleMat, peoplePoseSet

    newPeopleMat = [[[] for i in range(n)] for j in range(n)] 
    newPeoplePoseSet = set()
    # 여기에다가 모두 넣어놓고 한번에 peopleMat에 업데이트

    for cy,cx in peoplePoseSet:
        if len(peopleMat[cy][cx]) == 0:
            continue

        for curDir in peopleMat[cy][cx]:
            if distBtwSoole(cy,cx) > 3:
                newPeopleMat[cy][cx].append(curDir)
                newPeoplePoseSet.add((cy,cx))
                continue
            
            # 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
            ny, nx = cy+dys[curDir], cx+dxs[curDir]           
            if in_range(ny,nx) == True:
                # 움직이려는 칸에 술래가 있는 경우라면 움직이지 않습니다.
                if soolePose[:2] == [ny,nx]:
                    newPeopleMat[cy][cx].append(curDir)
                    newPeoplePoseSet.add((cy,cx))                    
                # 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동
                else:
                    newPeopleMat[ny][nx].append(curDir)
                    newPeoplePoseSet.add((ny,nx))            
            else:
                # 먼저 방향을 반대로 틀어줍니다. 
                curDir = (curDir+2)%4   
                ny, nx = cy+dys[curDir], cx+dxs[curDir]             
                # 이후 바라보고 있는 방향으로 1칸 움직인다 했을 때 해당 위치에 술래가 없다면 1칸 앞으로 이동합니다.
                if soolePose[:2] == [ny,nx]:
                    newPeopleMat[cy][cx].append(curDir)
                    newPeoplePoseSet.add((cy,cx))                    
                # 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동
                else:
                    newPeopleMat[ny][nx].append(curDir)
                    newPeoplePoseSet.add((ny,nx))
            # print(curDir,cy,cx, ny,nx)

    peopleMat = [[newPeopleMat[r][c][:] for c in range(n)] for r in range(n)]
    peoplePoseSet = newPeoplePoseSet.copy()

def moveSoole():
    global soolePose, reverse
    cy,cx,curDir = soolePose[:]
    ny, nx = cy+dys[curDir], cx+dxs[curDir]  

    dirInfo = [[0,3],[3,2],[2,1],[1,0]]
    if [ny,nx] == [0,0]:
        curDir = 3
        reverse = 1
    elif [ny,nx] == [n//2,n//2]:
        curDir = 1
        reverse = 0
    else:
        if ny < n//2 and nx-ny == 1:
            curDir = dirInfo[0][reverse]
        elif ny < n//2 and ny+nx == n-1:
            curDir = dirInfo[1][reverse]
        elif ny > n//2 and ny==nx:
            curDir = dirInfo[2][reverse]
        elif ny > n//2 and ny+nx == n-1:
            curDir = dirInfo[3][reverse]

        # 나선형 규칙 
        # (1,2) => 0 : (1,2) (0,1) : a,a+1 and a < n//2  1=>0, 2=>3
        # (1,3) => 3 : (1,3) (0,4) : y+x == 4 
        # (3,3) => 2 :             : a,a and a > n//2
        # (3,1) => 1               : y+x == 4 
        # (0,1)

    soolePose = [ny,nx, curDir]
    
def catch(t):
    global score, peopleMat

    cy,cx,curDir = soolePose[:]
    for i in range(3):
        ny,nx = cy+dys[curDir]*i, cx+dxs[curDir]*i
        if in_range(ny,nx) == False or treeMat[ny][nx] == True:
            continue
        score += (t * len(peopleMat[ny][nx]))
        peopleMat[ny][nx] = []




# 나무 위치 저장 mat
# 사람 pose 저장 mat (3차원) (dir 저장)
# 술래 pose 변수 (y,x,dir)

n,m,h,k = map(int, input().split())
treeMat = [[False for i in range(n)] for j in range(n)]
peopleMat = [[[] for i in range(n)] for j in range(n)] # 도망자 현재 방향 저장
peoplePoseSet = set() # 도망자 위치 저장
soolePose = [n//2, n//2,1]
reverse = 0

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

for i in range(m):
    y,x,d = map(int, input().split())
    curDir = 0
    if d == 1: # 좌우로 움직임
        curDir = 0 # 오른쪽 보고 시작
    elif d == 2: # 상하로 움직임
        curDir = 3 # 아래쪽 보고 시작
    peopleMat[y-1][x-1].append(curDir)
    peoplePoseSet.add((y-1,x-1))
for i in range(h):
    y,x = map(int, input().split())
    treeMat[y-1][x-1] = True

score = 0
for time in range(k):
    moveDomang()
    moveSoole()
    catch(time+1)
print(score)
