

# 억억단을 외우자 - 프로그래머스

def solution(e, starts):
    
    
    # 각각 곱한 결과를 저장
    infoList = [0 for i in range(e+1)]
    for r in range(1,e+1):
        for c in range(r, e+1): # 우상단 삼각형에 해당하는 곳만 계산함 (중복 제외하기 위해)
            val = r*c
            if(val > e):
                break
            
            # 둘이 같은 숫자면 한개만 추가
            if r == c:
                infoList[val] += 1
            else: # 다른 숫자면 순서 바꾸는 케이스도 있으니까 2개 추가 
                infoList[val] += 2
                
    # sort 없앰
    
    # dp 
    # min(starts)에서 e까지 모두 구해놓고
    # starts에 있는 인덱스를 가지고 numList에서 필요한 정보 읽어오도록 함 
    numList = [0 for _ in range(e+1)]
    maxNum = 0
    for i in range(e, min(starts)-1, -1): # e부터 거꾸로 시작해서 min(starts)까지만 진행 
        if infoList[i] >= maxNum:
            maxNum = infoList[i]
            numList[i] = i
        else:
            numList[i] = numList[i+1]  
    
    return [numList[i] for i in starts]
