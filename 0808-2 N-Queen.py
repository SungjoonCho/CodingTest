
# N-Queen 백준
# https://velog.io/@kjy2134/%EB%B0%B1%EC%A4%80-9663-N-Queen-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 백트래킹 문제


from collections import deque

n = int(input())

answer = 0

# 같은 열, 같은 대각선이면 아래처럼 대표 인덱스를 계산해서 해당 인덱스에 값이 채워졌는지 확인하는 방법으로 진행함
# 같은 열에 값이 있는지 확인은 각 열 인덱스 그대로 씀
# 정방향 대각선 특징 : 같은 대각선 상에 있는 애들은 r+c가 같음
# 역방향 대각선 특징 : 같은 대각선 상에 있는 애들은 r-c가 같음. 대신에 값이 n=4일경우 -3~3이 나와서 +n-1로 보정 필요

col_check = [0] * n # 같은 열인지 확인
check1 = [0] * (n*2-1) # r+c가 같은 애들
check2 = [0] * (n*2-1)  # r-c가 같은 애들

totalQueue = deque()

def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<n


def dfs(rIdx):
    global answer, totalQueue

    # 종료 조건
    if(rIdx == n):
        if(len(totalQueue) == n):
            # mat = [[0 for j in range(n)] for i in range(n)]
            # for each in totalQueue:
            #     mat[each[0]][each[1]] = 1
            # for i in mat:
            #     print(i)
            # print()
            answer += 1
        return

    # 열마다 체크
    for c in range(n):
        # 같은 열, 대각선 정방향 역방향 모두 1인게 없어야 됨
        if(col_check[c] == 0 and check1[rIdx+c] == 0 and check2[rIdx-c + n-1] == 0):
            col_check[c] = 1
            check1[rIdx + c] = 1
            check2[rIdx - c + n - 1] = 1
            totalQueue.append([rIdx, c])

            dfs(rIdx + 1)

            totalQueue.pop()
            col_check[c] = 0
            check1[rIdx + c] = 0
            check2[rIdx - c + n - 1] = 0



dfs(0)

print(answer)