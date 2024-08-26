
# 연구소2 - 백준
# https://www.acmicpc.net/problem/17141

# 백트래킹으로 조합 경우의 수 구하니까 시간초과 뜸
# 바이러스 위치 지정을 백트래킹 말고 combination 모듈 쓰니까 되네...

# comb 안쓰고 한 코드 : https://edder773.tistory.com/274
# mat 전체를 한줄로 만들어서 인덱싱할 수 있게 만들었음, 그래서 dfs 돌릴 때마다 mat을 어디서부터 볼지 시작점을 인자로 전달해줌
# 그리고 조합 만들려고 하는 백트래킹 과정에서 쓸데없이 append pop 안하네..
# 그냥 다이렉트로 mat에다가 숫자 넣었다가 백트래킹 할 때 원상복구시키고 이정도만 함




from collections import deque
from itertools import combinations

N, M = map(int, input().split())

mat = [[0 for c in range(N)] for r in range(N)]
virusPoses = []

blank = N*N
for r in range(N):
    mat[r] = list(map(int, input().split()))
    for c in range(N):
        if mat[r][c] == 2:
            virusPoses.append([r,c, 0]) #time
            mat[r][c] = 0
        elif mat[r][c] == 1:
            blank -= 1

used = [False for _ in range(len(virusPoses))]
time = float('inf')

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

temList = []

def in_range(y,x):
    return 0<= y and y<N and 0<=x and x<N

def bfs():
    global time, temList

    # temList = curVirusList[:] # 시간 추가
    curMat = [[mat[r][c] for c in range(N)] for r in range(N)]
    visited = [[False for c in range(N)] for r in range(N)]
    curBlank = blank
    for i in range(len(temList)):
        virRow, virCol, virTime = temList[i]
        curMat[virRow][virCol] = 2
        visited[virRow][virCol] = True
        curBlank -= 1

    temList = deque(temList)
    curTime = 0
    while temList:
        cy, cx, virTime = temList.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = cy+dy, cx+dx
            if not in_range(ny,nx) or mat[ny][nx] != 0 or visited[ny][nx] == True:
                continue

            temList.append([ny,nx, virTime+1])
            visited[ny][nx] = True
            curBlank -= 1
            curTime = virTime+1

    if curBlank == 0:
        time = min(curTime, time)


# def dfs(start):
#     global curVirusList, used
#
#     if len(curVirusList) == M:
#         bfs()
#         return
#
#     for i in range(start, len(virusPoses)):
#         if used[i] == False:
#             curR, curC = virusPoses[i]
#             used[i] = True
#             curVirusList.append([curR, curC])
#             dfs(start+1)
#             curVirusList.pop()
#             used[i] = False
#
# dfs(0)

whole_combinations = list(combinations(virusPoses, M))
for each in whole_combinations:
    temList = each[:]
    bfs()

if time == float('inf'):
    print(-1)
else:
    print(time)
