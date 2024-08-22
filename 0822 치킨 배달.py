
# 치킨 배달
# https://www.acmicpc.net/problem/15686


# 백트래킹, 브루트포스

n, m = list(map(int, input().split()))

homeList = []
chickenList = []
for r in range(n):
    row = list(map(int, input().split()))
    for c in range(n):
        if row[c] == 1:
            homeList.append([r,c])
        elif row[c] == 2:
            chickenList.append([r,c])
            
poseDiffMat = [[0 for i in range(len(chickenList))] for j in range(len(homeList))]

# 각 치킨집과 각 집 사이의 거리 측정해서 저장
for r in range(len(poseDiffMat)):
    for c in range(len(poseDiffMat[0])):
        poseDiffMat[r][c] = abs(chickenList[c][0]-homeList[r][0]) + abs(chickenList[c][1]-homeList[r][1])
    

# for i in poseDiffMat:
#     print(i)
# print()

chickenDistance = float('inf')
def dfs(startCol, selectedCol):
    global chickenDistance
    
    # 최대 m개일 때까지 모든 경우의 수에 대해 치킨 거리 계산 후 업데이트
    if 1<= len(selectedCol[0]):
        # for i in selectedCol:
        #     print(i)
        
        total = 0
        for r in range(len(selectedCol)):
            total += min(selectedCol[r])        
        chickenDistance = min(chickenDistance, total)
        
        # print(total)
        # print()
    
    if len(selectedCol[0]) == m:
        return
    
    # 열 선택
    for i in range(startCol, len(poseDiffMat[0])):
        dfs(i+1, [selectedCol[j] + [poseDiffMat[j][i]] for j in range(len(poseDiffMat))])
        
    
    
dfs(0, [[] for i in range(len(poseDiffMat))])

print(chickenDistance)
