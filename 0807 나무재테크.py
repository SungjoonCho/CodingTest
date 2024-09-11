# 나무 재테크 - 백준
# https://www.acmicpc.net/problem/16235

# 리스트로 할 경우
# 봄 여름 sort + len(칸 list) * N^2
# 가을 len(칸 list) * N^2
# 겨울 N^2

# NlogN + 2 * len(칸 list) * N^2 + N^2 = N^2 * (2 * len(칸 list) + 1)
# [ N^2 * (2 * len(칸 list) + 1) ] * k
# 각 칸에 나무 100개만 있어도 대략 20,000,000 (1초 전후) (근데 k가 1000까지 가면 나무 100개 훨씬 넘을듯)


# 딕셔너리로 할 경우
# 봄 여름 len(칸 key) * N^2
# 가을 len(칸 key) * N^2
# 겨울 N^2
# N^2 * len(칸 key) * k 

## 정렬을 하지 말라네


import sys

n,m,k = list(map(int, sys.stdin.readline().split()))

mat = [[{} for j in range(n)] for i in range(n)]
nu_mat = [[5 for j in range(n)] for i in range(n)]
new_nu_mat = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    new_nu_mat[i] = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    x,y,z = list(map(int, sys.stdin.readline().split()))
    x,y = x-1,y-1
    if(z not in mat[x][y].keys()):
        mat[x][y][z] = 0
    
    mat[x][y][z] += 1
    

dys = [0,-1,-1,-1,0,1,1,1]
dxs = [1,1,0,-1,-1,-1,0,1]

def in_range(y,x):
    return 0<=y and y<n and 0<=x and x<n
    
for game in range(k):
    # print()
    
    for r in range(n):
        for c in range(n):    
            nuVal = nu_mat[r][c]
            
            curInfo = list(mat[r][c].items()) # age, 개수
            # curInfo.sort(reverse=True)
            # print('aa', nuVal, curInfo)
            
            newDict = {}
            summerNu = 0
            while curInfo:
                cur = curInfo.pop()
                val = cur[0] * cur[1]
                if nuVal - val < 0:
                    
                    # 현재 선택된 cur 남은 것들 처리
                    age = cur[0]
                    cnt = cur[1]
                    while cnt > 0:
                        if nuVal - age < 0:
                            # cnt : 죽는 나무들 개수
                            summerNu += int(age // 2 * cnt)
                            # print('bb1', age // 2, cnt)
                            break
                        nuVal -= age
                        cnt -= 1
                        
                        # 아직 살아있는 애들은 newDict에 추가해야 되는데
                        if(age + 1 not in newDict.keys()): ### 여기를 안했네...
                            newDict[age + 1] = 0
                        newDict[age + 1] += 1
                    
                    # curInfo 에서 남은 것들 처리
                    while curInfo:
                        age, cnt = curInfo.pop()
                        # print('bb2', age // 2, cnt)
                        summerNu += int(age // 2 * cnt)                          
                    break
                
                nuVal -= val                    
                newDict[cur[0] + 1] = cur[1]
            
            
            mat[r][c] = newDict
            # 남은 양분 + 죽은 나무의 양분 업데이트
            nu_mat[r][c] = nuVal + summerNu
            # print('cc', nuVal, summerNu)
            
            
        
            
        # print(mat[r])
        
    for r in range(n):
        for c in range(n):    
            # 겨울 : 양분 추가
            nu_mat[r][c] += new_nu_mat[r][c]
            
            # 가을 : 나무 번식
            curInfo = list(mat[r][c].items()) # age, 개수
            if(len(curInfo) == 0):
                continue
            
            for each in curInfo:
                age, cnt = each
                if(age % 5 != 0):
                    continue                
                
                for dy, dx in zip(dys, dxs):
                    ny,nx = r+dy, c+dx
                    if(not in_range(ny,nx)):
                        continue                    
                    if 1 not in mat[ny][nx]:
                        mat[ny][nx][1] = 0
                    mat[ny][nx][1] += cnt
    

# 개수 세기
answer = 0
for r in range(n):
    for c in range(n):   
        curInfo = list(mat[r][c].items())
        if(len(curInfo) == 0):
            continue
            
        for each in curInfo:
            answer += each[1]

print(answer)


















######## deque로 진행

# import sys
# from collections import deque

# n,m,k = list(map(int, sys.stdin.readline().split()))

# mat = [[deque() for j in range(n)] for i in range(n)]
# nu_mat = [[5 for j in range(n)] for i in range(n)]
# new_nu_mat = [[0 for j in range(n)] for i in range(n)]
# dead_tree_mat = [[deque() for j in range(n)] for i in range(n)]

# for i in range(n):
#     new_nu_mat[i] = list(map(int, sys.stdin.readline().split()))

# for _ in range(m):
#     x,y,z = list(map(int, sys.stdin.readline().split()))
#     x,y = x-1,y-1    
#     mat[x][y].append(z)
    

# dys = [0,-1,-1,-1,0,1,1,1]
# dxs = [1,1,0,-1,-1,-1,0,1]

# def in_range(y,x):
#     return 0<=y and y<n and 0<=x and x<n
    
# def spring_summer():
#     global mat, nu_mat, dead_tree_mat
    
#     for r in range(n):
#         for c in range(n):
            
#             # 봄
#             length = len(mat[r][c])
#             if(length == 0):
#                 continue
            
#             nuVal = nu_mat[r][c]        
#             for i in range(length):
#                 if(nuVal < mat[r][c][i]):
#                     for _ in range(i, length):                        
#                         dead_tree_mat[r][c].append(mat[r][c].pop())
#                     break
#                 nuVal -= mat[r][c][i]
#                 mat[r][c][i] += 1
#             nu_mat[r][c] = nuVal
            
#             # 여름
#             while(dead_tree_mat[r][c]):
#                 val = dead_tree_mat[r][c].pop()
#                 nu_mat[r][c] += int(val//2)
                
# def fall_winter():
#     global mat, new_nu_mat, nu_mat
    
#     for r in range(n):
#         for c in range(n):
#             # 겨울 : 양분 추가
#             nu_mat[r][c] += new_nu_mat[r][c]
            
            
#             # 가을
#             length = len(mat[r][c])          
#             if(length == 0):
#                 continue
            
#             for i in range(length):                
#                 if(mat[r][c][i] % 5 == 0):
#                     for dy, dx in zip(dys, dxs):
#                         ny,nx = r+dy, c+dx
#                         if(not in_range(ny,nx)):
#                             continue
                        
#                         mat[ny][nx].appendleft(1)
                        
                
                
    
    
# for game in range(k):
    
#     spring_summer()
#     # for r in range(n):
#     #     print(mat[r])
#     # print()
    
#     fall_winter()
    
#     # for r in range(n):
#     #     print(mat[r])
#     # print()
    
    
# # 개수 세기
# answer = 0
# for r in range(n):
#     for c in range(n):   
#         answer += len(mat[r][c])

# print(answer)
