
# 스도쿠 - 백준

# 83퍼에서 계속 시간 초과 뜬 문제
# 수정 전 : blank 각 칸마다 들어갈 수 있는 숫자들의 개수를 계산하고, 최소 개수 갖고있는 애를 구하고 거기서 dfs 진행
# 수정 후 : blank 각 칸에 1~9까지 숫자를 하나씩 넣어보면서 check 함수들에 위배되면 넘기고, 통과하면 바로 다음 가지로 나아갈 수 있게 만듦

# 수정 전에는 매 iter마다 blank list에 있는 모든 요소들 확인해야 했지만, 수정 후에는 무작정 일단 가지 뻗고 시작해서 각 iter마다 연산 횟수는 작아짐


# 각 행, 열, 3x3 사각형 안에 num이 이미 있는지 없는지 확인
def check_row(r, num):
    for i in range(0,9):
        if mat[r][i] == num:
            return False
    return True

def check_col(c, num):
    for i in range(0,9):
        if mat[i][c] == num:
            return False
    return True

def check_square(r, c, num):

    rowRange = []
    colRange = []
    if (r < 3):
        if (c < 3):
            rowRange, colRange = [0, 2], [0, 2]
        elif (c < 6):
            rowRange, colRange = [0, 2], [3, 5]
        else:
            rowRange, colRange = [0, 2], [6, 8]
    elif (r < 6):
        if (c < 3):
            rowRange, colRange = [3, 5], [0, 2]
        elif (c < 6):
            rowRange, colRange = [3, 5], [3, 5]
        else:
            rowRange, colRange = [3, 5], [6, 8]
    else:
        if (c < 3):
            rowRange, colRange = [6, 8], [0, 2]
        elif (c < 6):
            rowRange, colRange = [6, 8], [3, 5]
        else:
            rowRange, colRange = [6, 8], [6, 8]

    for rr in range(rowRange[0], rowRange[1] + 1):
        for cc in range(colRange[0], colRange[1] + 1):
            if mat[rr][cc] == num:
                return False

    return True



def dfs(idx):
    global mat, cnt

    # 종료 조건
    if (cnt == 0):
        for r in range(9):
            for c in range(9):
                print(mat[r][c], end=' ')
            print()
        exit(0)

    r,c = blankList[idx]
    for num in range(1,10):
        if(check_row(r, num) and check_col(c,num) and check_square(r,c,num)):
            mat[r][c] = num
            cnt -= 1

            dfs(idx+1)

            mat[r][c] = 0
            cnt += 1


#################################################

mat = [[0 for i in range(9)] for j in range(9)]
blankList = []

for i in range(9):
    mat[i] = list(map(int, input().split()))
    for c in range(9):
        if mat[i][c] == 0:
            blankList.append([i, c])

cnt = len(blankList)
dfs(0)
