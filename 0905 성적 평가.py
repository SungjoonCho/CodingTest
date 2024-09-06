
# 성적 평가 - 소프티어
# https://softeer.ai/practice/6251

# 딕셔너리에 k:v = 점수 : [인덱스] 로 정리
# 딕셔너리를 리스트화 시켜서 정렬 
# [인덱스]의 개수대로 각 점수마다 등수 매길 수 있고, 올바른 인덱스에 등수를 입력할 수 있음

import sys

input = sys.stdin.readline
n = int(input())

finalScoreList = [0] * n
for eachCnt in range(3):
    numDict = {}
    numSet = set()
    numList = list(map(int,input().split()))
    for i in range(n):
        val = numList[i]
        if val not in numSet:
            numDict[val] = []
            numSet.add(val)
        numDict[val].append(i)
        finalScoreList[i] += val
    
    wholeList = [[k] + [v] for k,v in numDict.items()]
    wholeList.sort(reverse=True)
    rankList = [0] * n
    curLen = 1
    for j in range(len(wholeList)):      
        for k in range(len(wholeList[j][1])):
            r = wholeList[j][1][k]
            rankList[r] = curLen
        curLen += len(wholeList[j][1])    
    print(' '.join(map(str, rankList)))



numDict = {}
numSet = set()
numList = list(map(int,input().split()))
for i in range(n):
    val = finalScoreList[i]
    if val not in numSet:
        numDict[val] = []
        numSet.add(val)
    numDict[val].append(i)
    
wholeList = [[k] + [v] for k,v in numDict.items()]
wholeList.sort(reverse=True)
rankList = [0] * n
curLen = 1
for j in range(len(wholeList)):      
    for k in range(len(wholeList[j][1])):
        r = wholeList[j][1][k]
        rankList[r] = curLen
    curLen += len(wholeList[j][1])    
print(' '.join(map(str, rankList)))

