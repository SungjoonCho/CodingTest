
# 웜홀
# https://www.acmicpc.net/problem/1865



import sys
input = sys.stdin.readline


def bellman(start):
    dp = [2000000000] * (N+1)
    dp[start] = 0
    for i in range(N):
        for s,e in graphKey:
            t = graph[(s,e)]
            if dp[e] > dp[s] + t:
                dp[e] = dp[s] + t
                if dp[start] < 0:
                    return True 
                if i == N-1: # 마지막 회차면 (음의 사이클이라는 뜻 => 계속 작아질거임)
                    return True
    return False
                
    
tc = int(input())
for eachTc in range(tc):
    N, M, W = map(int, input().split())

    graph = dict()
    graphKey = set()
    for i in range(M):
        s,e,t = map(int, input().split())
        if (s,e) not in graphKey:
            graph[(s,e)] = 2000000000
            graphKey.add((s,e))
        if (e,s) not in graphKey:
            graph[(e,s)] = 2000000000
            graphKey.add((e,s))        
        graph[(s,e)] = min(graph[(s,e)], t)
        graph[(e,s)] = min(graph[(e,s)], t)
        
    for i in range(W):
        s,e,t = map(int, input().split())    
        if (s,e) not in graphKey:
            graph[(s,e)] = 2000000000
            graphKey.add((s,e))
        graph[(s,e)] = min(graph[(s,e)], -1*t)
        
    if bellman(1):    
        print('YES') 
    else:
        print('NO')
        
# 벨만포드 
        
# dp 초기화를 INF로 하면 시작 노드랑 분리된 노드들의 경우 음의 사이클이 있든없든 내려갈일이 없음, 
# 근데 적당히 큰 수로 하면 (문제 보고 정하기) 시작 노드랑 분리된 노드들이 가지는 간선들의 영향으로 dp 값이 INF가 아니라 정말로 감소하기 때문에 음의 사이클이 생길 수 있음
