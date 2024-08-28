

# 숨바꼭질2 - 백준
# https://www.acmicpc.net/problem/12851


from collections import deque

N,K = map(int, input().split())

# print(N, K)

# if N == K:
#     print(0)
#     exit(0)


dp = [0 for _ in range(100001)]
record = [0 for _ in range(100001)]

def in_range(x):
    return 0<=x and x<100001

queue = deque()
queue.append(N)
dp[N] = 1
record[N] = 1

while queue:
    curPose = queue.popleft()
    
    if dp[K] > 0 and dp[curPose] >= dp[K]:
        break
    
    for i in range(3):
        nextPose = 0
        if i == 0:
            nextPose = curPose - 1
        elif i == 1:
            nextPose = curPose + 1
        elif i == 2:
            if curPose > K:
                continue            
            nextPose = curPose * 2
            
        if not in_range(nextPose):
            continue
        
        if dp[nextPose] == 0:
            dp[nextPose] = dp[curPose]+1
            record[nextPose] = 1
            queue.append(nextPose)
        elif dp[nextPose] == dp[curPose]+1:
            record[nextPose] += 1  
            queue.append(nextPose)
            
print(dp[K]-1)
print(record[K])
        
