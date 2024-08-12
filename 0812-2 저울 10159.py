
# 저울 10159 - 백준



import sys

n = int(input())
m = int(input())

graph = {} # 큰 : 작
graph2 = {} # 작 : 큰

for i in range(m):
    big, small = list(map(int, sys.stdin.readline().split()))
    if big not in graph.keys():
        graph[big] = []
    graph[big].append(small)
    
    if small not in graph2.keys():
        graph2[small] = []
    graph2[small].append(big)
        
# print(graph2)




def dfs(i): #작은 숫자로
    global remain, used
    
    if(i not in graph.keys()):
        return
    
    for j in graph[i]:
        if used[j] == False:
            used[j] = True
            remain -= 1
            dfs(j)
            
def dfs2(i): # 큰 숫자로
    global remain, used
    
    if(i not in graph2.keys()):
        return
    
    for j in graph2[i]:
        if used[j] == False:
            used[j] = True
            remain -= 1
            dfs2(j)

# 각 숫자에서 시작해서 본인보다 작은 숫자로 이어지는 그래프, 큰 숫자로 이어지는 그래프 두개 탐색 후 남은 카운트 출력
# m(최대 2000) x 2 x n(최대 100) = 40만 < 1초(2000만) 

for i in range(1, n+1):
    
    used = [False for i in range(n+1)]
    remain = n-1        
    used[i] = True
    
    dfs(i)
    dfs2(i)
    print(remain)
        
