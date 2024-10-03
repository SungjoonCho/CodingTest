
# 강의실 배정
# https://www.acmicpc.net/problem/11000

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
timeline = []
for i in range(N):
    timeline.append(list(map(int,input().split())))
timeline.sort(key=lambda x:(x[0], x[1]))

room = []
heappush(room, timeline[0][1])
for i in range(1, N):
    start, end = timeline[i]
    if room[0] > timeline[i][0]:
        heappush(room,timeline[i][1]) # 새로운 강의실 열기
    else:
        heappop(room)
        heappush(room, timeline[i][1]) # 기존 강의실의 끝 시간 연장
print(len(room))


# heapq에 강의실 종료 시간 넣어놓고
# heapq[0] (=제일 빨리 끝나는 강의의 시간) 이 다음 강의 시작시간보다 늦으면 새 강의실 열기
# 일찍 끝나면 같은 강의실 쓰는거니까 그 수업은 꺼내고, 다음 수업 종료 시간 넣어주기
# heapq에 남아있는 강의 개수 출력 
