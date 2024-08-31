

# 왕실의 기사 대결 (코드트리)
# https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20



# temMat_bef에 기사 맵핑 (기사랑 벽만)(함정 말고)
# temMat_bef에서 bfs 진행 (미는 기사의 방향대로만 + 큐에 들어온 번호에 해당하는 기사)
    # 만약 여기에 벽이 들어오면 밀지 말기
    # bfs 하면서 들어오는 기사 번호만 따로 저장 (set)
# set에 있는 기사 번호애들만 knightList에서 좌표 이동

# temMat_aft에 기사 맵핑 (기사)
# 기존 저장된 함정 위치에 따라 기사의 체력 -1





L, N, Q = list(map(int, input().split()))
mat = [] # 빈칸, 벽만 저장
hamjungList = [[False for c in range(L)] for r in range(L)] # 함정 따로 저장
for i in range(L):
    row = list(map(int, input().split()))
    mat.append(row)
    for j in range(L):
        if mat[i][j] == 0:
            mat[i][j] = -1 # 빈칸은 -1로 바꿈
        elif mat[i][j] == 1:
            hamjungList[i][j] = True
            mat[i][j] = -1
        elif mat[i][j] == 2:
            mat[i][j] = -2 # 벽은 -2로 바꿈 (기사랑 번호 헷갈릴까봐)




knightList = []
for i in range(N):
    r,c,h,w,k = list(map(int, input().split()))
    knightList.append([r-1,c-1,h,w,k])

scoreList = [0 for i in range(len(knightList))]

kingCommand = []
for i in range(Q):
    i, d = list(map(int, input().split()))
    kingCommand.append([i-1, d])
# d는 0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽 방향을 의미합니다.

temMat_bef = [[0 for c in range(L)] for r in range(L)]

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def mapping(i, start_r, start_c, height, width):
    global temMat_bef
    # 0 1 2 1
    for r in range(start_r, start_r + height):
        for c in range(start_c, start_c+width):
            temMat_bef[r][c] = i

def check_hamjung(i, start_r, start_c, height, width):
    global knightList, scoreList

    for r in range(start_r, start_r + height):
        for c in range(start_c, start_c+width):
            if hamjungList[r][c] == True:
                knightList[i][-1] -= 1
                if knightList[i][-1] == 0:
                    scoreList[i] = 0
                    return
                scoreList[i] += 1

def in_range(y,x):
    return 0<=y and y<L and 0<=x and x<L

def spread_bfs(k_idx, k_r, k_c, k_dir):
    queue = []
    visited = [[False for c in range(L)] for r in range(L)]
    curKnightList = set()

    queue.append([k_idx, k_r, k_c])
    visited[k_r][k_c] = True
    curKnightList.add(k_idx)


    while queue:
        cur_idx, cur_r, cur_c = queue.pop(0)

        dIdx = -1
        for dy, dx in zip(dys, dxs):
            dIdx += 1

            ny, nx = cur_r+dy, cur_c+dx

            # 가려는 방향이 범위 밖인 경우
            if (in_range(ny,nx) == False and dIdx == k_dir):
                # print('return 1')
                return False, []

            # 그 외에 범위 밖이면
            if in_range(ny, nx) == False:
                continue

            if (temMat_bef[cur_r][cur_c] != temMat_bef[ny][nx] and dIdx != k_dir)\
                    or visited[ny][nx] == True \
                    or temMat_bef[ny][nx] == -1:
                continue

            # 범위 안이긴 한데 가려는 방향에 벽이 있는 경우
            if temMat_bef[ny][nx] == -2:
                return False, []

            n_idx = temMat_bef[ny][nx]
            queue.append([n_idx, ny, nx])
            visited[ny][nx] = True
            curKnightList.add(n_idx)

    return True, curKnightList



## Main ##

for qIdx in range(Q):
    # print('======================', qIdx)
    kingcmd = kingCommand[qIdx]
    k_idx, k_dir = kingcmd
    k_r, k_c, k_h, k_w, k_k = knightList[k_idx]
    if k_k <= 0: # 이미 사라짐
        continue

    temMat_bef = [[mat[r][c] for c in range(L)] for r in range(L)]
    for s_idx, eachKnight in enumerate(knightList):
        s_r, s_c, s_h, s_w, s_k = eachKnight
        if s_k <= 0:
            continue
        mapping(s_idx, s_r, s_c, s_h, s_w)

    res, pushKnightList = spread_bfs(k_idx, k_r, k_c, k_dir)
    if res == False:
        continue

    dy,dx = dys[k_dir], dxs[k_dir]
    for s_idx in pushKnightList:
        knightList[s_idx][0] += dy
        knightList[s_idx][1] += dx

        if(s_idx == k_idx):
            continue

        s_r, s_c, s_h, s_w, s_k = knightList[s_idx]
        # 새 위치에 함정 있는지 확인
        check_hamjung(s_idx, s_r, s_c, s_h, s_w)

print(sum(scoreList))


### 그냥 범위 밖으로 나가는 경우 있는지 체크
# 4 3 4
# 0 0 1 0
# 0 0 1 0
# 1 1 0 1
# 0 0 2 0
# 1 2 2 1 5
# 2 1 2 1 1
# 3 2 1 2 3
# 2 3
# 1 2
# 2 1
# 3 3
