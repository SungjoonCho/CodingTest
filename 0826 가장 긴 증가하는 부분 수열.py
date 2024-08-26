

# 가장 긴 증가하는 부분 수열 - 백준
# https://www.acmicpc.net/problem/11053


N = int(input())
ls = list(map(int, input().split()))

dp = [1 for i in range(len(ls))]

for i in range(len(ls)):
    for j in range(i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)        
print(max(dp))
