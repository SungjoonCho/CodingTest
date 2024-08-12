
# 회전 초밥 - 백준

# 슬라이딩 윈도우 방식 (크기 k의 윈도우)
# 윈도우 안에 c가 있으면 종류 개수만큼 가짐
# 윈도우 안에 c가 없으면 종류 개수 +1(쿠폰)

# 중복 여부는 used 배열로 체크


import sys

n,d,k,c = list(map(int, input().split()))

numList = []
for i in range(n):
    numList.append(int(input()))
# print(numList)


used = [0 for i in range(d+1)]
cnt = 0

# 초기화
start = 0
end = k - 1
for i in range(start, end+1):    
    num = numList[i]
    if used[num] == 0 :
        cnt += 1
    used[num] += 1 
    


# c가 없으면 + 1 
maxNum = cnt
if used[c] == 0:
    maxNum += 1

# print(start, end, used, maxNum)
        
for start in range(1, n):
    
    # end 업데이트
    end = end + 1
    if end == n:
        end = 0
    
    startNum = numList[start-1]
    endNum = numList[end]
    
    # 윈도우 shift
    used[startNum] -= 1
    if used[startNum] == 0:
        cnt -= 1        
    
    if used[endNum] == 0:
        cnt += 1
    used[endNum] += 1
    
    # c가 없으면 + 1 
    curCnt = cnt
    if used[c] == 0:
        curCnt += 1
    
    # 최대 갱신
    maxNum = max(maxNum, curCnt)
    
    # print(start, end, used, maxNum)
    
print(maxNum)
    
