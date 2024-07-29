# 퇴사2 - 백준 (2번째 풀어봄)
# https://www.acmicpc.net/problem/15486

N = int(input())
info = []

for i in range(N):
    info.append(list(map(int, input().split())))
    
dp = [0] * (N+1)

for i in range(1, N+1):
    
    dp[i] = max(dp[i], dp[i-1])
    
    t, p = info[i-1]
    if(i+t-1 > N):
        continue
    
    # (전날까지의 이익 + 오늘 상담 시작했을 때 얻는 이익)을 상담 끝나는 날에 기존 기록되어있는 이익과 비교해서 저장
    dp[i+t-1] = max(dp[i+t-1], dp[i-1]+p)

print(dp[-1])
# print(max(dp))