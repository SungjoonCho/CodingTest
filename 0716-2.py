


# 평범한 배낭 - 백준
# https://velog.io/@js43o/%EB%B0%B1%EC%A4%80-12865%EB%B2%88-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD 
# 참고함

n, maxWeight = list(map(int, input().split()))

dpMat = [[0 for i in range(n) ] for j in range(maxWeight+1)]

VList = []
for i in range(n):
    w, v = list(map(int, input().split()))    
    VList.append([w,v]) 
VList.sort()


# 2차원 테이블 만들어서
# 현재 열의 값, 이전 열의 값을 그대로 가져올지, (현재 최대 무게(기준) - 현재 무게)를 과거 기록 중 이전 아이템까지 탐색했을 때의 값
# 셋 중 max 값을 저장함

for r in range(1, len(dpMat)):    
    for c in range(0, len(dpMat[0])):
        
        if(c==0):           
            if(VList[c][0] <= r):
                dpMat[r][c] = VList[c][1]
            continue
        
        if(r - VList[c][0] < 0):
            dpMat[r][c] = max(dpMat[r][c-1], dpMat[r][c])
        else:
            dpMat[r][c] = max([dpMat[r][c-1], dpMat[r][c], dpMat[r-VList[c][0]][c-1] + VList[c][1]])


# for r in dpMat:
#     print(r)

print(dpMat[-1][-1])