
# 회의실 배정 - 백준


# 처음 생각 : 최고 끝시간까지의 방 개수로 구성된 리스트 만들어서 체크
# 최대 21억개 만들어질 수 있으므로 시간, 공간 복잡도 위배

# 다음 생각 : 그리디 활용
# [끝나는 시간 기준, 끝시간 시작시간 차이] 큰 순으로 정렬 후, 반복문 돌리면서 각 요소를 넣을지 말지를 각 회의의 시작 시간 확인하며 결정
# 각 회의의 시작시간이 이전 회의보다 늦게 있는지만 확인하면 됨, 다른 회의들 전체를 확인할 필요가 없어짐


# 시간 : nlogn + n : 60만


# print(2**31-1)

import sys
from collections import deque

n = int(input())
table = [0 for _ in range(n+1)]
edgeInfo = []

for i in range(n):
    s,e = map(int, sys.stdin.readline().split())
    edgeInfo.append([s,e])

edgeInfo.sort(key=lambda x:(x[1], -1*(x[1]-x[0])))


# print(edgeInfo)
edgeInfo = deque(edgeInfo)
_, maxE = edgeInfo.popleft()
cnt = 1

while edgeInfo:
    curS, curE = edgeInfo.popleft()

    if curS >= maxE and curE >= maxE:
        maxE = curE
        cnt += 1
    elif curS==maxE and curE==maxE: # max 끝시간이랑 현재 회의의 시작시간, 끝시간 같은 경우도 있으므로 조건 넣어줘야 됨
        maxE = curE
        cnt += 1

print(cnt)
