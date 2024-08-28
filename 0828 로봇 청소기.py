

# 로봇 청소기 - 백준
# https://www.acmicpc.net/problem/14503


def in_range(y,x):
    return 0<=y and y<N and 0<=x and x<M


N, M = list(map(int, input().split()))

init_r, init_c, init_dir = list(map(int, input().split()))

mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

dys = [-1,0,1,0]
dxs = [0,1,0,-1]

totalSum = 0
cleaned = [[0 for c in range(M)] for r in range(N)]




totalSum += 1
cleaned[init_r][init_c] = 1
cur_r, cur_c, cur_dir = init_r, init_c, init_dir

while True:
    
    init_dir = cur_dir
    
    canClean = False
    for _ in range(4):
        
        # 반시계로 회전
        if cur_dir - 1 == -1:
            cur_dir = 3
        else:
            cur_dir -= 1
        
        next_r = cur_r + dys[cur_dir] 
        next_c = cur_c + dxs[cur_dir]
        
        if not in_range(next_r, next_c) or mat[next_r][next_c] == 1:
            continue
        
        if cleaned[next_r][next_c] == 0:
            canClean = True
            cleaned[next_r][next_c] = 1
            totalSum += 1    
            cur_r, cur_c, cur_dir = next_r, next_c, cur_dir
            break
            
    if canClean == False:
        # 후진 방향으로 전환
        rear_dir = init_dir
        rear_dir -= 2
        if rear_dir < 0:
            rear_dir += 4
        
        next_r = cur_r + dys[rear_dir] 
        next_c = cur_c + dxs[rear_dir]
        
        if mat[next_r][next_c] == 1:
            break
        else:
            cur_r, cur_c, cur_dir = next_r, next_c, init_dir
            
            
print(totalSum)
