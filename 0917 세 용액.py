
# 세 용액 - 백준
# https://www.acmicpc.net/problem/2473

import sys

input = sys.stdin.readline
N = int(input())
infoList = list(map(int,input().split()))
infoList.sort()
# print(infoList)

absDiff = float('inf')
answer = []
for anchor in range(N-2):
    start = anchor + 1
    end = N-1
    while start < end:
        total = infoList[start] + infoList[end] + infoList[anchor]
        if abs(total) < absDiff:
            absDiff = abs(total)
            answer = [infoList[anchor], infoList[start], infoList[end]]

        if total < 0:
            start += 1
        else:
            end -= 1

print(" ".join(list(map(str,sorted(answer)))))


# https://wondev.tistory.com/138 참고
# 첫번째 용액을 반복문으로 하나씩 고정해놓고, 2번째 3번째 용액을 투포인터로 정함
