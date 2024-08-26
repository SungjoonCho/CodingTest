
# 경사로 - 백준
# https://www.acmicpc.net/problem/14890



def check(info):
    # 아닌 경우 발견하면 바로 reture False

    sameCnt = 1
    slope1 = False
    for i in range(1, N):
        
        # 왼쪽이 올라간 경우가 끝날 때
        if slope1 == True:

            if sameCnt == L:
                # 끝
                if info[i] - info[i-1] >= 1: # 구덩이에 갇힐 경우
                    return False
                
                # 원상복귀
                sameCnt = 0 # 여기서 0으로 해주고 아래 내려가서 1부터 채워주도록 해야 됨
                slope1 = False
            elif sameCnt < L and info[i - 1] != info[i]:
                return False



        # 평탄
        if info[i-1] == info[i]:
            sameCnt += 1

        # 오른쪽이 올라간 경우 
        elif info[i-1] < info[i]:
            if info[i] - info[i-1] == 1:
                # 경사로 끝
                if sameCnt < L:
                    return False
                sameCnt = 1
            else:
                return False
        
        # 왼쪽이 올라간 경우
        elif info[i - 1] > info[i]:
            if info[i-1] - info[i] == 1:
                # 경사로 시작
                sameCnt = 1
                slope1 = True
            else:
                return False


    if slope1 == True and sameCnt < L: # 하는 와중에 끝남
        return False

    return True





N,L = list(map(int, input().split()))
mat = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    mat[i] = list(map(int, input().split()))

totalCnt = 0
for r in range(N):
    # print(mat[r])
    res = check(mat[r])
    # print(r, res)
    if res == True:
        totalCnt += 1

# 90도 돌려서 한번 더
mat = list(map(list, zip(*mat[::-1])))
for r in range(N):
    # print(mat[r])
    res = check(mat[r])
    # print(r, res)
    if res == True:
        totalCnt += 1
        
print(totalCnt)
