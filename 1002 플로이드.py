# 플로이드 - 백준
# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
table = [[float('inf') for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    table[start][end] = min(table[start][end], cost) # 바로 저장

for k in range(1,n+1):
    table[k][k] = 0 # 자기한테 가는 거리는 0
    for start in range(1,n+1):
        for end in range(1,n+1):
            table[start][end] = min(table[start][end], table[start][k] + table[k][end])
            
for r in range(1,n+1):
    for c in range(1,n+1):
        val = table[r][c]
        if val == float('inf'):
            print(0, end=' ')
        else:
            print(val, end=' ')
    print()
    
# 플로이드 워셜
