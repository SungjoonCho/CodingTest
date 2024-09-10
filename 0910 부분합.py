
# 부분합 - 백준
# https://www.acmicpc.net/problem/1806

# 투포인터로 배열의 길이 조절하면서 해결

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
numList = list(map(int, input().split()))

start, end = 0,1
total = numList[start]
answer = 1e9
while start < end: 
    if total < S:
        if end < N:
            end += 1
            total += numList[end-1]
        else:
            break
    else:
        answer = min(end - start , answer)
        start += 1
        total -= numList[start-1]

if answer == 1e9: print(0)
else: print(answer)

