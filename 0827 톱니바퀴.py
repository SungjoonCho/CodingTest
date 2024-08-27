

# 톱니바퀴 - 백준
# https://www.acmicpc.net/problem/14891

from collections import deque


def in_range(x):
    return 0<=x and x<4

def bfs(dirList, start):

    queue = deque()
    queue.append(start)

    while queue:
        cx = queue.popleft()
        for dx in [-1,1]:
            nx = cx+dx
            if not in_range(nx) or dirList[nx] != 0:
                continue

            if dx == -1: # 왼쪽 바퀴를 봐야하면
                if mat[cx][6] != mat[nx][2]:
                    dirList[nx] = dirList[cx] * -1
                    queue.append(nx)
            elif dx == 1: # 오른쪽 바퀴 볼 때
                if mat[cx][2] != mat[nx][6]:
                    dirList[nx] = dirList[cx] * -1
                    queue.append(nx)

    return dirList[:]



mat = []
for i in range(4):
    mat.append( deque(list(map(int, list(input())))))

# print(mat)

rotationInfo = []
rotationCnt = int(input())
for i in range(rotationCnt):
    idx, direction = list(map(int, input().split()))
    rotationInfo.append([idx-1, direction])


for idx, direction in rotationInfo:
    dirList = [0 for _ in range(4)]
    dirList[idx] = direction

    # 각 바퀴의 회전 방향 결정
    dirList = bfs(dirList[:], idx)

    # 동시에 모든 바퀴 회전
    for i, eachDir in enumerate(dirList):
        if eachDir == 0:
            continue

        if eachDir == 1:
            val = mat[i].pop()
            mat[i].insert(0, val)
        elif eachDir == -1:
            val = mat[i].popleft()
            mat[i].append(val)

totalSum = 0
for i in range(4):
    if mat[i][0] == 0:
        continue
    totalSum += (2**i)

print(totalSum)


