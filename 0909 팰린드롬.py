

# 팰린드롬?
# https://www.acmicpc.net/problem/10942
# https://ddiyeon.tistory.com/73 참고

import sys

input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
M = int(input())

# 1,2개 일 때 초기화
# 2개일 때는 앞 뒤끼리만 확인하면 됨
dp = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    dp[i][i]=1
for i in range(N-1):
    if numList[i] == numList[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i + 1] = 0

# 3개부터는 첫 문자, 끝 문자 비교해서 다르면 펠린드롬 아님
# 첫 문자, 끝 문자 같다면 이전까지의 기록 dp[r+1][c-1] ( 첫 문자 인덱스+1 부터 끝 문자 인덱스 -1 까지 이미 검사한거)
# 이 0이면 펠린드롬 아님

for c in range(2,N):
    for r in range(N-c):
        if numList[r] == numList[c] and dp[r+1][c-1] == 1:
            dp[r][c] = 1

for interval in range(N-2):
    for i in range(N-2-interval):
        j = i+2+interval
        if numList[i]==numList[j] and dp[i+1][j-1]==1:
            dp[i][j]=1

# for i in dp:
#     print(i)

for i in range(M):
    s,e = map(int, input().split())
    print(dp[s-1][e-1])
