
# 나무 조경 - 소프티어
# https://softeer.ai/practice/7594
# 백트래킹 사용 


import sys

n = int(input())
mat = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    mat[i] = list(map(int, input().split()))

used = [[False for i in range(n)] for j in range(n)]
maxVal = 0
curVal = 0




dys = [0,1] # 오른쪽, 아래 (각 칸당 두 방향만 봐도 충분) 
dxs = [1,0]

def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<n

def dfs(cnt):
    global used, mat, maxVal, curVal

    
    # 종료 조건
    if(cnt == 4):
        return



    # anchor 정하기
    for r in range(n):
        for c in range(n):
            if(used[r][c] == False):      
                # 짝 정하기
                for dy, dx in zip(dys, dxs):
                    ny,nx = r+dy, c+dx
                    if(not in_range(ny,nx) or used[ny][nx] == True):
                        continue
                    # 짝까지 정해짐
                    
                    # 새로운 anchor
                    used[r][c] = True
                    curVal += mat[r][c]
                    # 짝
                    used[ny][nx] = True
                    curVal += mat[ny][nx]

                    # update 
                    maxVal = max(maxVal, curVal)
                    dfs(cnt+1)

                    # 해제
                    # 새로운 anchor
                    used[r][c] = False
                    curVal -= mat[r][c]
                    # 짝
                    used[ny][nx] = False
                    curVal -= mat[ny][nx]


dfs(0)
print(maxVal)

# print(2**16) 
