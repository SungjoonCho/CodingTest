
# 나무자르기 - 백준
# https://www.acmicpc.net/problem/2805



# 이분탐색
# sort 후
# 시작을 1, 끝을 나무 최고 높이로 두고 길이 조절해가면서 상근이가 최소로 원하는 나무 길이인 M을 얻을때까지 진행

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
treeList = list(map(int, input().split()))
treeList.sort()

start, end = 1, treeList[-1]
answer = 0
while start < end:
    mid = (start+end)//2
    totalSum = 0
    moveStart = False
    for i in range(N):
        if treeList[i] > mid:
            totalSum += (treeList[i] - mid)
        if totalSum >= M:
            moveStart = True
            answer = max(answer, mid)
            break
    if moveStart == True:
        start = mid + 1
    else:
        end = mid

print(answer)
