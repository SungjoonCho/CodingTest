
# 평범한 배낭 - 백준
# 냅색 문제 

N, K = list(map(int, input().split()))
info = []
for i in range(N):
    info.append(list(map(int, input().split()))) # 무게, 가치
    
dp = [[0 for i in range(N)] for j in range(K+1)] # 세로는 배낭의 최대무게, 가로는 물건 번호
# 배낭의 최대무게가 1씩 증가함에 따라 기록
# 물건을 1개씩 더 담으면서 기록

# 첫번째 열
for r in range(K+1):
    if r >= info[0][0]:
        dp[r][0] = info[0][1]
        
# 두번째 열부터
for c in range(1, N):
    for r in range(K+1):
        curWeight, curValue = info[c]
        if curWeight > r:
            dp[r][c] = dp[r][c-1]
            continue
        
        # 바로 이전까지의 물건들을 놓고 봤을 때 and 현재 최대 가방 크기 일 때의 가치 
        # 바로 이전까지의 물건들을 놓고 봤을 때 and 현재 최대 가방 크기 일 때의 가치에서 현재 물건 무게를 빼고 (확보시켜 놓고) 나머지 크기일 때의 최대 가치 + 현재 물건 가치
        dp[r][c] = max(dp[r][c-1], dp[r-curWeight][c-1]+curValue)
        
# for i in dp:
#     print(i)

print(dp[-1][-1])
