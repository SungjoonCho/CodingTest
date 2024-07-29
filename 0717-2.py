
# 가장 긴 감소하는 부분 수열 - 백준



# 각 수를 배열의 인덱스로 봄
# i를 볼 때 i에 저장된 기록과 max[i+1:]의 기록 +1 을 비교

# max를 계속 해도 되네..
# 그럼 시간복잡도 N^2 
        
N = int(input())
info = list(map(int, input().split()))
maxTotal = max(info)


dp = [0 for i in range(maxTotal+1)]


for i in range(len(info)):
    num = info[i]
    if(num == maxTotal):
        dp[num] = 1
        continue
    
    dp[num] = max(dp[num], max(dp[num+1:])+1) 
    
answer = max(dp)
print(answer)
        
        
        
        
# # i번째랑 max[i+1:]+1 을 비교
        
        
# N = int(input())
# info = list(map(int, input().split()))
# maxTotal = max(info)


# dp = [0 for i in range(maxTotal+1)]


# # prev = 0
# # maxNum = 0
# for i in range(len(info)):
#     num = info[i]
#     if(num == maxTotal):
#         dp[num] = 1
#         continue
    
#     # if(i == 0 or maxNum < num or num == maxTotal):
#     #     maxNum = num # 현재까지의 최대값
#     #     dp[num] = 1
#     # else:    
#     dp[num] = max(dp[num], max(dp[num+1:])+1) #dp[num] = max(dp[num], max(dp[num+1:maxNum+1])+1)
    
#     # prev = num
    
# # print(dp)

# answer = max(dp)
# # if(answer == 1):
# #     print(0)
# # else:
# print(answer)
        