
# 오큰수
# https://www.acmicpc.net/problem/17298

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    array = list(map(int, input().split()))
    dp = [-1 for i in range(N)]
    for i in range(N-2, -1, -1):
        next_i = i+1
        while next_i <= N-1:
            if array[i] < array[next_i]:
                dp[i] = array[next_i]
                break
            elif array[i] < dp[next_i]:
                dp[i] = dp[next_i]
                break
            elif dp[next_i] == -1:
                dp[i] = -1
                break
            else:
                next_i += 1
    for i in dp:
        print(i, end=' ')
main()

# DP



## 다른사람풀이 (스택 사용)
# import sys
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# NGE= [-1]*N
# stack = [0] # 0번 인덱스
#
# for i in range(1, N):
#     # 오큰수 : A[i]의 오른쪽에 있으면서 A[i]보다 큰 수 중 가장 왼쪽 값
#     while stack and A[stack[-1]] < A[i]:
#         NGE[stack.pop()] = A[i] # 해당 인덱스 칸은 A[i]
#     stack.append(i)
# print(*NGE)

# 내 풀이는 (작은 값)이 주인공이고,
# 이 풀이는 비교당하는 (큰 값)이 주인공임
