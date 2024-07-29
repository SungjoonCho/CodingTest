
# 퇴사 - 백준

N = int(input())

infoList = []

for i in range(N):
    infoList.append(list(map(int, input().split())))
    
dp = [0 for i in range(N+1)]

for eachDay in range(N-1, -1, -1):
    
    # 상담한다 가정했을 때 상담 마치는 날 -1 (1 뺀 이유는 상담기간은 당일도 포함하니까) 이 N-1보다 클 경우 하면 안됨
    if(eachDay + infoList[eachDay][0] - 1 > N-1):
        dp[eachDay] = dp[eachDay+1]
        
    else: # 상담 안했을 때, 상담 했을 때 비교 (현재 날짜의 이익 + 현재날짜의 상담 기간이 지나고 났을 때의 저장된 값 불러오기)
        # 여기서는 1 빼줄 필요없음 (당일 + a 일 지나고 나서의 날이니까)
        dp[eachDay] = max(dp[eachDay+1], infoList[eachDay][1] + dp[eachDay + infoList[eachDay][0]]) 
        
    # print(dp[eachDay])

print(dp[0])