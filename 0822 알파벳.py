# 알파벳 - 백준
# https://www.acmicpc.net/problem/1987

# dfs + 백트래킹 (pypy)


# bfs로 진행하되 set 이용해서 다음 알파벳이 현재까지의 문자열에 존재하는지 (in) 체크하면 파이썬으로 가능하다 함 (https://leeingyun96.tistory.com/22)
# set의 in은 O(1) 리스트는 최악일 때 O(N) 

from collections import deque

R,C = list(map(int, input().split()))
mat = []

for _ in range(R):
    mat.append(input())
    
alphaList = [False for _ in range(26)]

dys = [0,-1,0,1]
dxs = [1,0,-1,0]

def in_range(y,x):
    return 0<=y and y<R and 0<=x and x<C

maxCnt = 0
def dfs(curPose, cnt):
    global maxCnt, alphaList
    
    maxCnt = max(maxCnt, cnt)
    # print(cnt)
    
    cy, cx = curPose
    # print(cy,cx, mat[cy][cx], cnt) 
    # print(mat[cy][cx])
    for dy, dx in zip(dys, dxs):
        ny,nx = cy+dy, cx+dx
        
        # print(ord(mat[ny][nx])-65)
        if not in_range(ny,nx) or alphaList[ord(mat[ny][nx])-65] == True:
            # print(alphaList)
            
            continue
        
          
        alphaList[ord(mat[ny][nx])-65] = True
        dfs([ny,nx], cnt+1)
        alphaList[ord(mat[ny][nx])-65] = False
        
alphaList[ord(mat[0][0])-65] = True       
dfs([0,0], 1)
print(maxCnt)
