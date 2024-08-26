#
#
# # 나무 자르기 - 백준
# # https://www.acmicpc.net/problem/2805
#
#
# # 딕셔너리로 같이 높이의 나무끼리 개수 구해놓고 하나씩 pop해서 누적합으로 구함
#
# N,M = map(int, input().split())
#
# trees = list(map(int, input().split()))
#
# treeInfo = {} # 나무 높이마다 개수 저장
# treeKey = set() # 나무 높이 저장
# for i in trees:
#     if i not in treeKey:
#         treeKey.add(i)
#         treeInfo[i] = 0
#     treeInfo[i] += 1
#
# treeInfo = list(map(list, treeInfo.items()))
# treeInfo.sort()
#
# totalSum = 0
# while True:
#     # print(treeInfo)
#     # print(totalSum)
#
#     # 제일 큰 나무부터 pop
#     curHeight1, cnt1 = treeInfo.pop()
#     if len(treeInfo) == 0:
#         while True:
#             totalSum += cnt1
#             curHeight1 -= 1
#             if totalSum >= M:
#                 print(curHeight1)
#                 exit(0)
#
#     # 다음으로 큰 나무와의 차이 구해서 개수 곱하고 총합에 누적
#     curHeight2, cnt2 = treeInfo[-1]
#     temSum = totalSum + ((curHeight1 - curHeight2) * cnt1)
#
#     # 만약 그게 목표치 M보다 크면 높이 1당 나무 개수씩 누적
#     if temSum > M:
#         for curHeight in range(curHeight1-1, curHeight2-1, -1):
#             totalSum += cnt1
#             # print(curHeight, totalSum)
#             if totalSum >= M:
#                 print(curHeight)
#                 exit(0)
#     elif temSum == M:
#         print(treeInfo[-1][0])
#         exit(0)
#
#     # 다음 나무 높이의 개수에 현재 높이의 나무 개수를 누적
#     totalSum = temSum
#     treeInfo[-1][1] += cnt1
#



# https://www.acmicpc.net/problem/2805
# 이분탐색 활용해서도 풀수있음 ( https://data-flower.tistory.com/99 )

N,M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, sum(trees)
while start <= end:
    mid = (end+start) // 2

    totalSum = 0
    for t in trees:
        if t > mid:
            totalSum += (t-mid)

    if totalSum >= M:
        start = mid+1
    else:
        end = mid-1

print(end)
