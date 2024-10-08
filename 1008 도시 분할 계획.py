

# 도시 분할 계획 - 백준
# https://www.acmicpc.net/problem/1647

import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
edges = []
parent = [i for i in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key = lambda x:x[2]) # 간선 오름차순 정렬

answer = 0
last_edge = 0
for a,b,c in edges:
    if find(a) != find(b): # 이미 같은 그룹인거는 안들어감 (edges를 간선 값 순서로 정렬했기 때문에 안 들어가도 됨) = answer에 추가 안됨
        union(a,b)
        answer += c
        last_edge = c # 마지막 간선은 제거해도 됨 (얘 아니었으면 a,b가 같은 그룹이 아니었을거임)

print(answer - last_edge)

# 크루스칼 알고리즘
# 유니온 파인드
# https://velog.io/@sihoon_cho/BOJ%EB%B0%B1%EC%A4%80-1647%EB%B2%88-%EB%8F%84%EC%8B%9C-%EB%B6%84%ED%95%A0-%EA%B3%84%ED%9A%8D-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%92%80%EC%9D%B4
