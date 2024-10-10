

# Strahler 순서

import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for t in range(T):
    K, M, P = map(int, input().split())
    graph = [set() for i in range(M+1)]
    graphCnt = [0 for i in range(M+1)]
    graphOrder = [[1,0] for i in range(M+1)]
    for p in range(P):
        start, end = map(int, input().split())
        graph[start].add(end)
        graphCnt[end] += 1

    queue = deque()
    for i in range(1,len(graphCnt)):
        if graphCnt[i] == 0:
            queue.append([i, 1])

    while queue:
        curNode, curCnt = queue.popleft()
        for end in graph[curNode]:
            graphCnt[end] -= 1
            if graphOrder[curNode][0] > graphOrder[end][0]:
                graphOrder[end][0] = graphOrder[curNode][0]
                graphOrder[end][1] = 1
            elif graphOrder[curNode][0] == graphOrder[end][0]:
                graphOrder[end][1] += 1

            if graphCnt[end] == 0:
                if graphOrder[end][1] >= 2:
                    graphOrder[end][0] += 1
                    queue.append([end, graphOrder[end][0]+1])
                elif graphOrder[end][1] == 1:
                    queue.append([end, graphOrder[end][0]])
    print(K, graphOrder[M][0])


# 위상정렬 
