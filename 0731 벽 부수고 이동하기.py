# 벽 부수고 이동하기 - 백준

from collections import deque

n, m = list(map(int, input().split()))
mat = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    mat[i] = list(map(int, list(input())))

dys = [0, -1, 0, 1]
dxs = [1, 0, -1, 0] ##



# 말이 되고픈 원숭이.py 와 유사한 문제
# 각 grid 칸마다 정보를 2개 넣을 수 있음 - 현재 칸까지 올 때까지 벽을 부순 적 있는지 없는지에 따른 최단 거리 (3차원 필요)
# bfs 진행 

# 리스트 queue로 하면 시간 초과, deque로 하니까 괜찮음 



def in_range(y, x):
    return 0 <= y and y < n and 0 <= x and x < m

def bfs():
    
    # bfsMat,visited 2차원에 0은 벽 부순 적 X, 1은 O

    queue = deque()
    bfsMat = [[[0] * 2 for i in range(m)] for j in range(n)]
    visited = [[[False] * 2 for i in range(m)] for j in range(n)]

    queue.append([0,0,0])
    bfsMat[0][0][0] = 1
    visited[0][0][0] = True

    while (queue):
        cy, cx, cd = queue.popleft() # cd는 depth

        if(cy == n-1 and cx == m-1):
            return bfsMat[cy][cx][cd]

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if (not in_range(ny, nx) or visited[ny][nx][cd] == True):
                continue


            if(cd == 0):
                if(mat[ny][nx] == 0):
                    bfsMat[ny][nx][cd] = bfsMat[cy][cx][cd] + 1
                    queue.append([ny, nx, cd])
                    visited[ny][nx][cd] = True
                elif(mat[ny][nx] == 1):
                    bfsMat[ny][nx][1] = bfsMat[cy][cx][cd] + 1
                    queue.append([ny, nx, 1])
                    visited[ny][nx][1] = True

            elif(cd == 1 and mat[ny][nx] == 0):
                bfsMat[ny][nx][1] = bfsMat[cy][cx][cd] + 1
                queue.append([ny, nx, 1])
                visited[ny][nx][1] = True

    # for i in bfsMat:
    #     print(i)

    return -1

result = bfs()

print(result)
