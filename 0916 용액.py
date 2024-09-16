
# 용액 - 백준
# https://www.acmicpc.net/problem/2467

import sys

input = sys.stdin.readline
N = int(input())
infoList = list(map(int,input().split()))

absDiff = float('inf')
seList = []
start,end = 0, len(infoList)-1
while start < end:
    val = infoList[start] + infoList[end]
    if abs(val) < absDiff:
        absDiff = abs(val)
        seList = [infoList[start], infoList[end]]
    if val < 0:
        start += 1
    else:
        end -= 1

print(" ".join(list(map(str, sorted(seList)))))

# 투 포인터 문제
