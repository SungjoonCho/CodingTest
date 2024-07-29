# # 1로 만들기 - 백준
# https://jominseoo.tistory.com/98 참고

n = int(input())


dp = [0] * 1000001 # 연산 횟수 저장

if(n >= 2):
    for i in range(2,n+1):
        
        dp[i] = dp[i-1] + 1
        
        if(i%2 == 0):
            dp[i] = min(dp[i], dp[i//2]+1)

        if(i%3 == 0):
            dp[i] = min(dp[i], dp[i//3]+1)
        
print(dp[n])

    




# n = int(input())

# list1 = []
# list2 = []
# list3 = []

# bigNum = None 

# if(n==1):
#     print(0)
#     exit()

# # 초기화
# if(n%3 == 0):
#     list1.append(n//3)
# else:
#     list1.append(bigNum)

# if(n%2 == 0):
#     list2.append(n//2)
# else:
#     list2.append(bigNum)
    
# list3.append(n-1)

# cnt = 1

# if(list1[0] == 1 or list2[0] == 1 or list3[0] == 1):
#     print(cnt)
#     exit()


# while True:
#     cnt += 1
#     temList = [list1[-1], list2[-1], list3[-1]]
    
    
    
#     saveList = []
#     for n in temList:        
#         if(n == None):
#             continue                
#         elif(n%3 == 0):
#             saveList.append(n//3)
            
#     if(len(saveList) == 0):
#         list1.append(None)
#     else:            
#         list1.append(min(saveList))
        
#     if(list1[-1] == 1):
#         break
            
            
#     saveList = []
#     for n in temList:        
#         if(n == None):
#             continue                
#         elif(n%2 == 0):
#             saveList.append(n//2)
            
#     if(len(saveList) == 0):
#         list2.append(None)
#     else:            
#         list2.append(min(saveList))
        
#     if(list2[-1] == 1):
#         break
        
        
        
#     saveList = []
#     for n in temList:        
#         if(n == None):
#             continue                       
#         saveList.append(n-1)
            
#     if(len(saveList) == 0):
#         list3.append(None)
#     else:            
#         list3.append(min(saveList))
        
#     if(list3[-1] == 1):
#         break
    
# print(list1)
# print(list2)
# print(list3)
# print(cnt)



