
# 두 배열의 합 - 백준
# https://www.acmicpc.net/problem/2143

import sys
import collections

input = sys.stdin.readline

T = int(input())
n = int(input())
aList = list(map(int, input().split()))
m = int(input())
bList = list(map(int, input().split()))

aTotalList = []
bTotalList = []
for i in range(n):
    prevSum = 0
    for j in range(i,n):
        prevSum += aList[j]
        aTotalList.append(prevSum)
for i in range(m):
    prevSum = 0
    for j in range(i,m):
        prevSum += bList[j]
        bTotalList.append(prevSum)

aDict = collections.Counter(aTotalList)
bDict = collections.Counter(bTotalList)
bKeySet = set(bDict.keys())

answer = 0
for k,v in aDict.items():
    if T-k not in bKeySet:
        continue
    answer += (v * bDict[T-k])
print(answer)

