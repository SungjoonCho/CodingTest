
# 숨바꼭질3 - 백준
# https://www.acmicpc.net/problem/1697

from collections import deque

N,K = map(int, input().split())

# print(N, K)

if N == K:
    print(0)
    exit(0)


dp = [0 for _ in range(100001)]
used = [False for _ in range(100001)]

def in_range(x):
    return 0<=x and x<100001

queue = deque()
queue.append(N)
used[N] = True

while queue:
    curPose = queue.popleft()
    
    for i in range(3):
        jump = False
        nextPose = 0
        
        if i == 0:
            nextPose = curPose - 1
        elif i == 1:
            nextPose = curPose + 1
        elif i == 2:
            if curPose > K:
                continue            
            nextPose = curPose * 2
            jump = True
            
            
        if not in_range(nextPose):
            continue
        
        if dp[nextPose] == 0 and used[nextPose] == False:
            if jump == False:
                dp[nextPose] = dp[curPose]+1                
            else:
                dp[nextPose] = dp[curPose]
            queue.append(nextPose)
            used[nextPose] = True
        else: # 이미 used True임
            if jump == False and dp[nextPose] > dp[curPose]+1:
                dp[nextPose] = dp[curPose]+1
                queue.append(nextPose)       
            elif jump == True and dp[nextPose] > dp[curPose]:
                dp[nextPose] = dp[curPose]
                queue.append(nextPose)    
    
        
print(dp[K])
# print(dp[:100])
