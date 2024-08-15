
# 줄세우기 - 백준
# 위상정렬

# 각 노드 본인에 붙어있는 엣지들이 빨리 사라질수록 앞에 옴
# 본인한테 붙어있는 엣지 개수를 recv에 저장 ([a,b]가 input으로 주어지면 b에 저장)

# 아예 연결이 안된 노드들이 있을 수도 있음
# 그래서 queue에 recv가 0인 케이스 모두 넣어놓고 시작해서 강제로 출력하게 만듦


from collections import deque
import sys

n, m = list(map(int, input().split()))
recv = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = list(map(int, sys.stdin.readline().split()))

    graph[a].append(b)
    recv[b] += 1

# 아예 연결이 안된 노드들이 있을 수도 있음
# recv 0인 애들만 따로 queue에 저장해놓고 시작
blankList = deque()
for i in range(1, len(recv)):
    if(recv[i] == 0):
        blankList.append(i)


while blankList:

    curNode = blankList.popleft()
    print(curNode, end=' ')

    # 각 노드에 연결된 다른 노드들의 recv 1씩 감소시켜주고
    # 0 되면 출력 후보에 추가
    for i in range(len(graph[curNode])):
        val = graph[curNode][i]
        recv[val] -= 1
        if recv[val] == 0:
            blankList.append(val)


