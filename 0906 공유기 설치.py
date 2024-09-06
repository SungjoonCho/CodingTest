
# 공유기 설치
# https://www.acmicpc.net/problem/2110


# https://www.acmicpc.net/problem/2110

# 집들 사이의 최소 거리와 최대 거리의 중앙을 이용한 이분탐색
# => 공유기 사이의 거리를 딱 정해놓고 시작, 각 기준 거리 케이스마다 놓을 수 있는 공유기 개수 세고 원하는 공유기 개수보다 많냐 적냐에 따라서 기준 거리를 조절하면 됨
# (이때 start, end 조절하면 돼서 이분탐색 쓰라는거임)


import sys

input = sys.stdin.readline
N,C = map(int, input().split())
houseList = []
for i in range(N):
    houseList.append(int(input()))
houseList.sort()


start, end = 1, houseList[-1] - houseList[0]
result = 0
if C == 2:
    print(houseList[-1]-houseList[0])
    exit(0)
while start < end:
    midDist = (start+end)//2
    prev = houseList[0]
    cnt = 1
    for i in range(1,N):
        if houseList[i] - prev >= midDist:
            cnt += 1
            prev = houseList[i]

    if cnt >= C: # c보다 많다는 것은 그만큼 공유기 사이 거리가 촘촘하다는 것 => midDist를 늘려야 됨 => 집간 최소 거리인 start를 키워야됨
        start = midDist+1
        result = midDist
    else:
        end = midDist

print(result)

