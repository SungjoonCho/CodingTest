
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
