
# 최소비용 구하기 - 백준
# https://www.acmicpc.net/problem/1916

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())
graph = [set() for _ in range(N+1)]
dp = [INF] * (N+1)
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].add((end, cost))
depart, arrive = map(int, input().split())

heapq = []
visited = [False] * (N+1)

heappush(heapq, [0, depart])
visited[depart] = True
dp[depart] = 0
while heapq:
    curSum, curNode = heappop(heapq)
    for nextNode, cost in graph[curNode]:
        if visited[nextNode] == True:
            continue
        if curSum + cost < dp[nextNode]:
            heappush(heapq, [curSum + cost, nextNode])
            dp[nextNode] = curSum + cost
print(dp[arrive])

# 다익스트라 
