
# 타임머신 - 백준

# 벨만포드

N, M = list(map(int, input().split()))

busInfo = []
for i in range(M):
    busInfo.append(list(map(int, input().split())))
    
# print(busInfo)

distResult = [float('inf') for i in range(N+1)]

def bellman():
    
    distResult[1] = 0
    
    # N개의 노드가 있을 때 특정 노드에서 나머지 노드들 N-1개로 최단거리로 가는 것이 목표
    # 그래서 모든 엣지 순회를 N-1번만 진행하면 갈 수 있는 모든 노드를 최단거리로 갈거임
        # 처음에 못가던 노드도 하나씩 하나씩 뚫리고 게속 하다보면 전체 갈수있게 되는거임..
        
    # 그렇게 N-1번 반복해서 최단거리 구했겠지 했는데
    # N번째 순회 때 최단 거리 업데이트가 가능하면 그거는 음수 순환이라 해서 무한정 업데이트가 일어날 수 있는거임
    # 엣지가 음수이고 사이클 돌 때마다 계속 작아져버리는것
    
    for i in range(N):
        for j in range(M):
            depart_node, arrive_node, edge_cost = busInfo[j]
            # depart_node -= 1
            # arrive_node -= 1
            
            if distResult[depart_node] != float('inf') and distResult[arrive_node] > distResult[depart_node] + edge_cost:
                distResult[arrive_node] = distResult[depart_node] + edge_cost

                # 음수 순화 판별 
                if i == N-1:
                    return False 
    
    return True


res = bellman()
if res == False:
    print(-1)
else:
    # print(distResult)
    for i in range(2, len(distResult)):
        if distResult[i] == float('inf'):
            print(-1)
        else:
            print(distResult[i])
