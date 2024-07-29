# 택배 배달과 수거하기 - 프로그래머스


# delivery, pickup 리스트 각각 관리, 각 리스트의 인덱스를 한번만 방문하도록 함
# 각 리스트를 가장 큰 인덱스부터 확인하고 합산해서 cap 값 될 때까지 반복, 각 리스트에서 값 빼기
# (위에서 구해진 가장 큰 인덱스+1) * 2를 distance에 합산
# 이 과정 반복 (가장 최근 방문한 인덱스부터 다시 시작)

def solution(cap, n, deliveries, pickups):
    distance = 0
    last_deliIdx = n - 1
    last_puIdx = n - 1

    while True:

        # print(last_deliIdx, last_puIdx)

        # print(deliveries)
        # print(pickups)
        # print()

        deliCap, puCap = cap, cap
        maxDist_deli, maxDist_pu = 0, 0  # 현재 최대 거리 배송지, 수거지 중 최대 거리 구하기 위함

        start = False

        # 가장 먼 곳부터 탐색 (최근에 탐색한 곳부터 시작)
        for i in range(last_deliIdx, -1, -1):
            deliCnt = deliveries[i]
            last_deliIdx = i

            if (deliCnt == 0):
                continue
            elif (start == False):  # deliCnt 양수이면서, 제일 먼 배송지라면
                maxDist_deli = i + 1
                start = True

            if (deliCnt <= deliCap):
                deliCap -= deliCnt
                deliveries[i] = 0
            else:  # 현재 집에서 원하는만큼 모두 배송 못하는 경우
                deliveries[i] -= deliCap
                deliCap = 0

                # 더 이상 배송 못하는 경우
            if (deliCap == 0):
                break

        start = False
        for i in range(last_puIdx, -1, -1):
            puCnt = pickups[i]
            last_puIdx = i

            if (puCnt == 0):
                continue
            elif (start == False):
                maxDist_pu = i + 1
                start = True

            if (puCnt <= puCap):
                puCap -= puCnt
                pickups[i] = 0
            else:
                pickups[i] -= puCap
                puCap = 0

            if (puCap == 0):
                break

        distance += max(maxDist_deli, maxDist_pu) * 2

        # print(last_deliIdx, last_puIdx)
        # 배송 끝
        if (last_deliIdx == 0 and last_puIdx == 0):  # 아직 0번째에 값 남아있을 수 있음
            if (sum(deliveries) == 0 and sum(pickups) == 0):  # 각 리스트에 남은 값 있는지 확인
                return distance


