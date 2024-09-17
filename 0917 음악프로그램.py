
# 음악프로그램 - 백준
# https://www.acmicpc.net/problem/2623


import sys
from collections import deque

input = sys.stdin.readline
N, M = list(map(int, input().split()))
info = dict()
for i in range(N+1):
    info[i] = []
cntList = [0] * (N+1)

for i in range(M):
    temList = list(map(int, input().split()))
    for j in range(len(temList[1:])-1):
        key = temList[1+j]
        value = temList[1+j+1]
        info[key].append(value)
        cntList[value] += 1

answer = []
queue = deque()
for i in range(1, len(cntList)):
    if cntList[i] == 0:
        queue.append(i)

while queue:
    i = queue.popleft()
    answer.append(i)
    for j in info[i]:
        cntList[j] -= 1
        if cntList[j] == 0:
            queue.append(j)

if len(answer) == N: # ansewr에 있는 가수 명수가 가수 총 명수랑 같아야 제대로 위상 정렬된거임 
    for i in answer:
        print(i)
else:
    print(0)
    

# 위상 정렬로 해결
# 각 노드 본인한테 오는 엣지의 개수가 0이 되어야 print 가능
# 앞에 오는 가수일수록 연결된 엣지 개수가 빨리 0이 될것이고, 뒤에 오는 가수일수록
# 엣지가 늦게 사라져서 연결된 엣지 개수가 늦게 0이될거임.
