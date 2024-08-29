

# 할로윈의 양아치 - 백준

# 용우님 코드 참고함 

import sys
from sys import setrecursionlimit

setrecursionlimit(10**5) 
input = sys.stdin.readline

N,M,K = list(map(int, input().split()))
candyList = [0] + list(map(int, input().split()))


# 양방향으로 정보를 추가해줘야 됨
graph = [set() for i in range(N+1)] # 요소 중복되지 않는 것 보장되면 리스트 대신 set 쓰는게 좋음
for i in range(M):
    start, end = map(int,input().split())
    graph[start].add(end)
    graph[end].add(start)

# print(candyList)
# print(graph)

candyPackage = []
used = [False] * (N+1)


# 덩어리 묶기
totalSum, idxCnt = 0,0
def dfs(start):
    global totalSum, idxCnt

    totalSum += candyList[start]
    idxCnt += 1
    for j in graph[start]:
        if used[j] == False:
            used[j] = True
            dfs(j)

for i in range(1, N+1):
    if used[i] == False:
        totalSum, idxCnt = 0,0
        used[i] = True
        dfs(i)
        if idxCnt < K:
            candyPackage.append([totalSum, idxCnt])

# print(candyPackage)

# 냅색 알고리즘으로 해결 가능 (DP)
dp = [0] * K
for candy, children in candyPackage:
    for i in range(K-1, -1, -1):
        if dp[i] > 0 and i+children < K:
            dp[i+children] = max(dp[i+children], dp[i] + candy)
    dp[children] = max(dp[children], candy)
    print(dp)

print(max(dp))

