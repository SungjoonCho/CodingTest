
# 1,2,3 더하기 - 백준

## DFS
# T = int(input())

# cnt = 0

# def dfs(idx, baseList):
#     global cnt
    
#     if(idx+1 == len(baseList)):
#         return
    
#     val = baseList[idx] + baseList[idx+1]
#     if(val > 3):
#         return
    
#     bef_val = baseList[idx+1]
#     baseList[idx+1] = val
#     cnt += 1
    
#     for i in range(idx+1, n-1):
#         dfs(i, baseList[:])
    
#     baseList[idx+1] = bef_val
    

# for _ in range(T):
    
#     n = int(input())
    
#     baseList = [1 for i in range(n)]
#     cnt = 1  
#     for i in range(n-1):
#         dfs(i, baseList[:])    
#     print(cnt)


## DP

T = int(input())


for _ in range(T):
    n = int(input())
    
    resList = [1,2,4]
    
    if(n <= 3):
        print(resList[n-1])
    else:
        for i in range(3,n):
            resList.append(resList[i-1] + resList[i-2] + resList[i-3])
        print(resList[-1])
    
    