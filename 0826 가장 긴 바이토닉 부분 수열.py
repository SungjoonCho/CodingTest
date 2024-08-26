

# 가장 긴 바이토닉 부분 수열 - 백준
# https://www.acmicpc.net/problem/11054


N = int(input())
ls = list(map(int, input().split()))

dp1 = [1 for i in range(len(ls))]
for i in range(len(ls)):
    for j in range(i):
        if ls[i] > ls[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

# print(dp)        
# print(max(dp1))

dp2 = [1 for i in range(len(ls))]
for i in range(len(ls)-1, -1, -1):
    for j in range(i+1, len(ls)):
        if ls[i] > ls[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
    
totalMax = 0        
for i in range(len(dp1)):
    totalMax = max(totalMax, dp1[i] + dp2[i] -1)    

print(totalMax)
