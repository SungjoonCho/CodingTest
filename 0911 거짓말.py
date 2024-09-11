# 거짓말 - 백준
# https://www.acmicpc.net/problem/1043


# 진실을 아는 그룹과 모르는 그룹 분리해야 됨
# 모든 엣지를 노드 양방향으로 추가해서 그래프 표현
# 그리고 재귀 함수에 진실 아는 노드 하나씩 넣어주면서 관련된 모든 사람들 visited 처리

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())

realList = list(map(int, input().split()))
realN = realList[0]
realList = realList[1:]

totalPartyInfo = []
info = [set() for i in range(N+1)]   
for i in range(M):
    partyInfo = list(map(int, input().split()))   
    partyN = partyInfo[0]
    partyList = partyInfo[1:]  
    totalPartyInfo.append([partyN, partyList])
    if partyN > 1:
        for j in partyList[1:]:
            info[partyList[0]].add(j)
            info[j].add(partyList[0])
    
visited = [False] * (N+1)
def dfs(startIdx):    
    global visited
    
    if len(info[startIdx]) == 0:
        return    
    for j in info[startIdx]:
        if visited[j] == True:
            continue
        visited[j] = True
        dfs(j)
        

for i in range(realN):
    eachRealIdx = realList[i]
    visited[eachRealIdx] = True
    dfs(eachRealIdx)

answer = 0
for i in range(M):    
    partyN, partyList = totalPartyInfo[i][0], totalPartyInfo[i][1]
    
    can = True
    if partyN == 1:
        idx = partyList[0]
        can = not visited[idx]
    else:        
        for j in range(partyN):
            idx = partyList[j]
            if visited[idx] == True:
                can = False
                break    
            
    if can == True:
        answer += 1
        
print(answer)
