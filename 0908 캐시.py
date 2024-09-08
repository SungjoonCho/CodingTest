# 캐시 - 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/17680#

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
            
    prev = set()
    queue = deque()    
        
    for c in cities:
        c = c.lower()        
        if c not in prev:
            if len(queue) == cacheSize:
                prev.remove(queue.popleft())            
            prev.add(c)
            queue.append(c)
            answer += 5
        else: # 이미 있을 경우       
            tem_queue = list(queue)
            tem_queue.remove(c)
            queue = deque(tem_queue)
            queue.append(c)       
            answer += 1
            
    return answer
