
# 퍼즐
# https://www.acmicpc.net/problem/1525

import sys
from collections import deque
input = sys.stdin.readline

def in_range(y,x):
    return 0<=y and y<3 and 0<=x and x<3

def convert_toStr():
    global mat

    string = ''
    for r in range(3):
        for c in range(3):
            string += mat[r][c]
    return string

def bfs():
    global mat

    queue = deque()
    visited = set()
    curState = convert_toStr()
    visited.add(curState)
    queue.append([curState, 0])

    while queue:
        curState, curCnt = queue.popleft()
        i = curState.index('0')
        cy,cx = int(i)//3, int(i)%3

        mat = []
        for r in range(3):
            mat.append(list(curState[r*3:r*3+3]))
        for dy,dx in zip([0,-1,0,1],[1,0,-1,0]):
            ny, nx = cy+dy, cx+dx
            if not in_range(ny,nx):
                continue

            mat[ny][nx], mat[cy][cx] = mat[cy][cx], mat[ny][nx]
            if convert_toStr() == '123456780':
                return curCnt+1
            nextState = convert_toStr()
            if nextState not in visited:
                queue.append([nextState, curCnt+1])
                visited.add(nextState)
            mat[cy][cx], mat[ny][nx] = mat[ny][nx], mat[cy][cx]


mat = []
for i in range(3):
    mat.append(list(input().strip().split()))

curState = convert_toStr()
if curState == '123456780':
    print(0)
    exit(0)
elif len(set(curState)) < 9:
    print(-1)
    exit(0)

curCnt = bfs()
if curCnt != None:
    print(curCnt)
else:
    print(-1)


# 3x3 퍼즐을 일렬 문자열로 저장
# 자리를 바꿔서 생길 수 있는 케이스들을 bfs로 확장해나가면서 생각 (각 경우의 수 mat을 문자열로 변환해서 queue에 추가)


# https://velog.io/@dhelee/%EC%9D%BC%EC%9D%BC%EC%BD%94%ED%85%8C-Day14
