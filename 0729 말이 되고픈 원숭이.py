# 말이 되고픈 원숭이
# https://www.acmicpc.net/problem/1600

# bfs, dp 활용 (말처럼 움직였을 때, 안 움직였을 때 나눠서 저장)


from collections import deque

k = int(input())
w, h = list(map(int, input().split()))



if(w==1 and h==1):
    print(0)
    exit()

infoMat = []
for i in range(h):
    row = list(map(int, input().split()))
    infoMat.append(row)
    
    


dys = [0,-1,0,1]
dxs = [1,0,-1,0]
dys2 = [-1,-2,-2,-1, 1,2,2,1]
dxs2 = [-2,-1,1,2, -2,-1,1,2]

def in_range(y,x):
    return 0<=y and y<h and 0<=x and x<w



# 3차원으로 풀어야됨 = 행 열 이동횟수
# resultMat => 결과 저장

def bfs():
    
    resultMat = [[[0] * (k+1) for c in range(w)] for r in range(h)]
    
    queue = deque()
    queue.append([0,0,0])
    resultMat[0][0][0] = 1


    while(queue):
            
        cy, cx, ck = queue.popleft()

        if(cy == h-1 and cx == w-1):
            print(resultMat[cy][cx][ck]-1)
            exit()
        
        # 원숭이 방향
        for dy, dx in zip(dys,dxs):
            ny, nx = cy+dy, cx+dx
            
            if(not in_range(ny,nx) or resultMat[ny][nx][ck] != 0 or infoMat[ny][nx] == 1):
                continue
            
            resultMat[ny][nx][ck] = resultMat[cy][cx][ck] + 1
            queue.append([ny,nx,ck])
            
            
        # 말 방향
        if(ck < k):
            for dy, dx in zip(dys2,dxs2):
                ny, nx = cy+dy, cx+dx
                
                if(not in_range(ny,nx) or resultMat[ny][nx][ck+1] != 0 or infoMat[ny][nx] == 1 ):
                    continue            
                            
                resultMat[ny][nx][ck+1] = resultMat[cy][cx][ck] + 1
                queue.append([ny,nx,ck+1])                    
                
            
    # for i in resultMat:
    #     print(i)
    # print()

bfs()
print(-1)

