# 양과 늑대- 프로그래머스

def solution(info, edges):
    answer = []
    
    visited = [False] * len(info)
    def dfs(sheep, wolf):
        
        if sheep > wolf:
            # answer = max(answer, sheep)
            answer.append(sheep)
        else: # 더 진행하면 안됨 (양 <= 늑대)
            return
        
        for s,e in edges: # edge 전체를 매dfs마다 반복하면서 모든 경우의 수에 대해 체크
            if visited[s] == True and visited[e] == False:
                visited[e] = True
                if info[e] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[e] = False
    
    visited[0] = True
    dfs(1,0)
    
    
    return max(answer)


