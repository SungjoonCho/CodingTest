# 최소 비용 구하기 - 백준
# https://velog.io/@ssh00n/%EB%B0%B1%EC%A4%80-1916-%EC%B5%9C%EC%86%8C%EB%B9%84%EC%9A%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98


# 다익스트라로 해결
# heap에 최소비용, 노드 정보 넣어놓고
# 하나씩 비용 작은 것을 heappop 하면서 현재 비용 + 뽑은 엣지 비용이 다음 노드에 저장된 값보다 작은지 확인
# 반복하면서 갱신 

import sys
import heapq

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

test = list(map(int, input().split()))
costs = [1e9 for i in range(N+1)]
heap = []

costs[test[0]] = 0
heapq.heappush(heap, [0,test[0]])

while heap:
    curCost, curNode = heapq.heappop(heap)
    if costs[curNode] < curCost:
        continue

    for nextV, nextCost in graph[curNode]:
        sumCost = curCost + nextCost
        if sumCost >= costs[nextV]:
            continue

        costs[nextV] = sumCost
        heapq.heappush(heap, [sumCost, nextV])

print(costs[test[1]])
