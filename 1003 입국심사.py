# 입국심사 - 프로그래머스

def solution(n, times):
    answer = 0    
    
    start = 1
    end = 1000000000000000001
    while start < end:
        mid = (start + end) // 2 # 전체 소요 시간
        total = 0 # 가능한 사람 수 
        for t in times:
            total += (mid // t)
            if total >= n:
                break
                
        if total >= n:
            end = mid
        else:
            start = mid+1        
        answer = start
    
    return answer

# 문제에서 요구하는 답을 타겟으로 잡기 
