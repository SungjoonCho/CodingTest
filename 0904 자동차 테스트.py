# 자동차 테스트 - 소프티어
# https://softeer.ai/practice/6247

import sys

def main():
    input = sys.stdin.readline   
    n, q = list(map(int, input().split()))
    numList = list(map(int, input().split()))
    numList.sort()
    numSet = set(numList)
    
    for _ in range(q):
        targetNum = int(input())
        if targetNum not in numSet:
            print(0)
            continue
            
        startIdx = 0
        endIdx = n-1
        medianIdx = 0
        while True:
            medianIdx = (startIdx+endIdx)//2
            if numList[medianIdx] == targetNum:                
                break
                
            if numList[medianIdx] < targetNum:
                startIdx = medianIdx+1
            else:
                endIdx = medianIdx-1
        print((n-medianIdx-1)*(medianIdx))
        
main()
    
