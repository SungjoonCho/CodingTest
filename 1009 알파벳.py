
# 알파벳 - 2번째 
# https://www.acmicpc.net/problem/1987

import sys
from collections import deque
input = sys.stdin.readline

def convertToIdx(string):
    return ord(string)-65

def in_range(y,x):
    return 0<=y and y<R and 0<=x and x<C

def dfs(cy, cx, curCnt):
    global maxVal
    maxVal = max(maxVal, curCnt)
    for dy, dx in zip([0, -1, 0, 1], [1, 0, -1, 0]):
        ny, nx = cy + dy, cx + dx
        if not in_range(ny, nx) or exist[convertToIdx(mat[ny][nx])] == True:
            continue
        exist[convertToIdx(mat[ny][nx])] = True
        dfs(ny, nx, curCnt+1)
        exist[convertToIdx(mat[ny][nx])] = False

R,C = map(int, input().split())
mat = []
for i in range(R):
    mat.append(list(input()))
maxVal = 1
exist = [False for i in range(26)]
exist[convertToIdx(mat[0][0])] = True
dfs(0,0, 1)
print(maxVal)


# 파라미터를 재귀로 매번 많이 넘겨주는건 지양하자

# 이렇게 지나온 길을 기록해둬야 하는 문제는 가능하면 백트래킹으로 하자




import sys
input = sys.stdin.readline

def in_range(y,x,R,C):
    return 0<=y and y<R and 0<=x and x<C

def main():
    R,C = map(int, input().split())
    mat = []
    for i in range(R):
        mat.append(list(input()))
    queue = set()
    queue.add((0,0, mat[0][0]))
    maxVal = 1
    while queue:
        cy, cx, curSet = queue.pop()
        maxVal = max(maxVal, len(curSet))
        for dy,dx in zip([0,-1,0,1], [1,0,-1,0]):
            ny,nx = cy+dy, cx+dx
            if not in_range(ny,nx,R,C) or mat[ny][nx] in curSet:
                continue
            queue.add((ny, nx, curSet + mat[ny][nx]))

    print(maxVal)
main()


# bfs로 됨
# 근데 mat[ny][nx]의 알파벳이 현재까지 지나온 문자열 중에 겹치는 것 있는지만 확인하고 queue에 넣는 식으로 하면 시간 초과임

# mat[ny][nx]까지 서로 다른 경로로 이동해도 ny, nx에 도착했을 떄 동일한 문자열, 동일한 횟수로 도착할 수 있음 - 이렇게 중복되는 경우들은 시간 복잡도 증가시킴
# 그래서 queue를 set으로 해줘서 중복 방지까지 해줘야 함
