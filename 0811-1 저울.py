# 저울 - 백준

# https://seongonion.tistory.com/127 참고함

# 처음에 정렬 후
# 누적합을 구하다가 새로운 수가 나왔을 때 못 만드는 수가 나오려면
# 그 새로운 수가 일정 크기 이상 커야 됨. 그래야 중간에 빈공간이 생겨서 못만드는 수가 생김
# 새로운 수가 현재까지의 누적합+1보다 크면 됨
# 새로운수+1 해도 누적합과 새로운수+1 사이의 수를 만족시킬수없을거니까

import sys

n = int(input())
inputList = list(map(int, sys.stdin.readline().split()))

inputList.sort()

curSum = 1
for num in inputList:
    if curSum < num:
        break
    curSum += num

print(curSum)
