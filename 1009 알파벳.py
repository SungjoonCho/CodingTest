
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
# 근데 deque 쓰면 시간초과 남

# 선입선출이 필요한 경우 deque 쓰는게 맞지만
# 이 문제는 선입선출이 필요없음.. 한번 방문한 곳을 또 방문하지 말라는 법 없음
# 그래서 deque 필요없고, 그냥 set과 pop 쓰면 시간 초과 해결됨
# 오히려 curSet에서 문자열 탐색은 신경 안썼네
