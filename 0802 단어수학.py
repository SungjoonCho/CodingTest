# 단어수학 - 백준

n = int(input())

# 각 알파벳의 자리에 따라 10^n이라는 값 부여하고 
# 같은 알파벳끼리 모두 값 합산 

alphaDict = {}
for i in range(n):
    alpha = list(input())
    
    for j in range(len(alpha)):
        curAlpha = alpha[j]
        # print(curAlpha)
        if(curAlpha not in alphaDict.keys()):
            alphaDict[curAlpha] = 0
        
        alphaDict[curAlpha] += (10**(len(alpha)-j-1))    
# print(alphaDict)

alphaList = []
for k,v in alphaDict.items():
    alphaList.append([k,v])

alphaList.sort(key=lambda x:x[1], reverse=True)
# print(alphaList)

# 가장 합산값이 큰 애부터 9 부여, 순차적으로 작은 수 부여 
curNum = 9
result = 0
for eachList in alphaList:
    result += (curNum * eachList[1])
    curNum -= 1

print(result)
