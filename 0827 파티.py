

# 파티 - 백준



# 다익스트라 (heapq 활용)
# https://steadily-worked.tistory.com/661 참고함

import sys
import heapq


def dijikstra(start):

    queue = []
    heapq.heappush(queue, [0, start]) # cost, start번 노드
    mat[start][start] = 0
    while queue:
        cost, curNode = heapq.heappop(queue)
        if mat[start][curNode] < cost:
            continue

        for nextIdx, nextCost in edgeList[curNode]:
            if cost + nextCost < mat[start][nextIdx]:
                heapq.heappush(queue, [cost + nextCost, nextIdx])
                mat[start][nextIdx] = cost + nextCost



N, M, X = list(map(int, input().split()))
edgeList = {}
for i in range(N+1):
    edgeList[i] = []

for _ in range(M):
    s,e,c = list(map(int, sys.stdin.readline().split()))
    edgeList[s].append((e,c))

# print(edgeList)

mat = [[float('inf') for i in range(N+1)] for j in range(N+1)]

# 각 노드를 출발지로 했을 때 나머지 노드들에 대한 최단거리 구하고
# 이거를 모든 노드들을 출발지로 해서 진행
# 그러면 각 노드가 X노드까지의 최단거리가 나올것이고, X노드에서도 다른 노드들로 최단거리 나옴
for i in range(1, N+1):
    dijikstra(i)

# for i in mat:
#     print(i)

maxTime = 0
for i in range(1, N+1):
    time = mat[i][X] + mat[X][i]
    maxTime = max(maxTime, time)
print(maxTime)
