
# 징검다리 건너기(small) - 백준

# queue에다가 갈 수 있는 다음 돌 인덱스를 넣어주되, 한 번 넣어준 적 있는 돌은 제외시킴
# queue에서 나온 돌이 목적지일 때까지 반복 

import sys
from collections import deque

n,k = list(map(int, sys.stdin.readline().split()))
inputList = list(map(int, sys.stdin.readline().split()))
used = [False for i in range(n)]

queue = deque()
queue.append(0)

while(queue):
    # print(queue)
    i = queue.popleft()

    for j in range(i+1, n):
        if(j-i > k):
            break

        if((j-i)*(1+abs(inputList[i]-inputList[j])) <= k):
            # 종료조건
            if (j == n - 1):
                print('YES')
                exit(0)

            if(used[j] == False):
                queue.append(j)
                used[j] = True

print('NO')
