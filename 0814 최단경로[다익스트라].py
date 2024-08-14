
# 최단경로 [다익스트라] - 백준
# https://sungmin-joo.tistory.com/33 참고함
# heapq 필요, 2차원 리스트 관리 필요 , 다익스트라

import sys
# from collections import deque
import heapq


vCnt,eCnt = list(map(int, input().split()))
startV = int(input())
graph = [[] for i in range(vCnt+1)]

# 2차원 리스트에 엣지 정보 저장 (2차원 테이블 안 만들고, 단순하게 바로 저장하면 메모리 아낌) (대신 2차원 내에서의 순서는 보장 못함)
for i in range(eCnt):
    u,v,w = list(map(int, sys.stdin.readline().split()))

    i# 중복 고려하지 않고 일단 넣음 (나중에 heapq에서 가중치 작은거를 고르니까 상관 X)
    graph[u].append((v,w))


# print(graph)




### 다익스트라
# 한 정점에서 다른 정점들로의 최소값을 구하기 위함
# 빠르게 최소 값을 구해놓을수록 heap에 쓸데없는 (노드에 저장된 값보다 큰 경우) 경우가 들어가지를 않음
# 그래서 기존에 내가 한 방식인 선입선출 큐보다 훨씬 연산량 줄어들을 수 있는 듯
dp = [float('inf') for i in range(vCnt+1)]

heap = []
heapq.heappush(heap, [0, startV]) # edge합산, 시작점

while(heap):

    curScore, curV = heapq.heappop(heap) # 최소 엣지 값 뽑아주기 위해 heap 사용

    if curScore > dp[curV]: # 다른것들이 앞에 많이 나와서 그 사이에 dp[curv]가 작아졌을 수 있음
        continue

    for nextV, nextScore in graph[curV]:
        ns = curScore + nextScore
        if ns < dp[nextV]:
            dp[nextV] = ns
            heapq.heappush(heap, [ns, nextV])


for i in range(1,vCnt+1):
    if i == startV:
        print(0)
    elif dp[i] == float('inf'):
        print("INF")
    else:
        print(dp[i])


