
# 미로 - 백준
# https://www.acmicpc.net/problem/24463


# bfs로 목적지까지의 최단 경로 구하는 동시에 이전 지점 기록
# 목적지에서부터 저장된 기록 따라서 시작 지점으로 이동

# # 용우님 코드 참고  : visited에 이전 지점 기록해두면 역으로 다시 갈 때 쓰기 좋음
# 출발지는 (-1, -1)로 해두고 목적지에서 출발지로 다시 돌아왔는지 판별은 (-1,-1) 왔는지 여부로 판단

# 모든 변수를 함수화 시키면 훨씬 빨라짐

from collections import deque


def main():
    se_points = []
    dys = [0, -1, 0, 1]
    dxs = [1, 0, -1, 0]

    N, M = map(int, input().split())
    mat = []
    for r in range(N):
        mat.append(list(input()))
        for c in range(M):
            if mat[r][c] == '.':
                mat[r][c] = '@'
                if c == 0 or c == M-1 or r==0 or r==N-1:
                    se_points.append([r, c])
    visited = [[None] * M for r in range(N)]
    startPose, endPose = se_points[:]


    def in_range(y, x):
        return 0 <= y and y < N and 0 <= x and x < M

    def bfs():
        queue = deque()
        queue.append(startPose)
        visited[startPose[0]][startPose[1]] = (-1, -1)

        while queue:
            cy, cx = queue.popleft()
            for dy, dx in zip(dys, dxs):
                ny, nx = cy + dy, cx + dx
                if not in_range(ny, nx) or visited[ny][nx] != None or mat[ny][nx] == '+':
                    continue
                queue.append([ny, nx])
                visited[ny][nx] = (cy, cx)  # 다음 경로에 현재 지점 정보 넣어줌

    def goBack(curPose):
        curR, curC = curPose[:]
        while (curR, curC) != (-1, -1):
            mat[curR][curC] = '.'
            curR, curC = visited[curR][curC]

    bfs()
    goBack(endPose[:])
    for i in range(N):
        print("".join(mat[i]))

main()
