# 계단 오르기 - 백준

n = int(input())

stairList = []
for i in range(n):
    stairList.append(int(input()))
    
    
# 전 계단(1가지), 전전 계단에서 온 경우(2가지)들 중에서 max 값을 연속 1개 계단인지 2개 계단인지에 따라 나눠서 저장

dp1 = [] # 전 계단에서 경우에 현재 계단 합산
dp1.append(stairList[0])

dp2 = [] # 전전 계단에서 온 경우에 현재 계단 합산
dp2.append(0)

if(n >= 2): # n은 300 이하 자연수임 => 1, 2가 올 수도 있음
    dp1.append(stairList[1])
    dp2.append(dp1[0] + stairList[1])

    for i in range(2, n): # n이 3 이상일 경우부터 적용
        
        val1 = dp1[i-2] + stairList[i]
        val2 = dp2[i-2] + stairList[i]
        dp1.append(max(val1, val2))
        
        dp2.append(dp1[i-1] + stairList[i])
        # dp2[i-1]은 읽어오면 안됨 (연속 3개를 가는거니까)
        
    # print(dp1)
    # print(dp2)

print(max(dp1[n-1], dp2[n-1]))
    
    