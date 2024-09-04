
# 효도 음식 - 소프티어
# https://softeer.ai/practice/7367


import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    numList = list(map(int, input().split()))

    
    # 현재까지의 합보다 현재 값이 크면 대체 
    dp1 = [-1001] * n
    dp1[0] = numList[0]
    for i in range(1, n):
        dp1[i] = max(numList[i], dp1[i-1] + numList[i])
    
    dp2 = [-1001] * n
    dp2[-1] = numList[-1]
    for i in range(n-2, -1 ,-1):
        dp2[i] = max(numList[i], dp2[i+1] + numList[i])
        
    
    # 현재 시점에 큰 값이 무엇인지 저장 (우로 가면서, 좌로 가면서)
    leftDp = [-1001] * n
    leftMax = dp1[0]
    for i in range(n):        
        leftMax = max(leftMax, dp1[i])
        leftDp[i] = leftMax
    
    rightDp = [-1001] * n
    rightMax = dp2[-1]
    for i in range(n-1, -1, -1):        
        rightMax = max(rightMax, dp2[i])
        rightDp[i] = rightMax
    
    # 각 시점마다 좌우를 봤을 때 최대값을 더해서 저장 해놓고 제일 큰 값이 뭔지 파악
    result = []
    for i in range(1, n-1):
        result.append(leftDp[i-1] + rightDp[i+1])
    print(max(result))
    
main()
