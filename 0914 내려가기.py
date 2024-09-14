

# 내려가기 - 백준
# https://www.acmicpc.net/problem/2096

# 1차원 DP

import sys

input = sys.stdin.readline
N = int(input())
dpMax = [0,0,0]
dpMin = [0,0,0]
for i in range(N):
    curList = list(map(int,input().split()))
    if i == 0:
        dpMax = curList[:]
        dpMin = curList[:]
        continue
    temDpMax = dpMax[:]
    temDpMin = dpMin[:]

    dpMax[0] = max(temDpMax[0], temDpMax[1]) + curList[0]
    dpMax[1] = max(temDpMax) + curList[1]
    dpMax[2] = max(temDpMax[1], temDpMax[2]) + curList[2]

    dpMin[0] = min(temDpMin[0], temDpMin[1]) + curList[0]
    dpMin[1] = min(temDpMin) + curList[1]
    dpMin[2] = min(temDpMin[1], temDpMin[2]) + curList[2]

print(max(dpMax), min(dpMin))
