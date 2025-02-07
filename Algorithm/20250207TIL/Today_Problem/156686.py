import sys
from itertools import combinations

# sys.stdin.readline을 사용하여 빠른 입력을 처리합니다.
input = sys.stdin.readline

# 도시의 크기 N과 선택할 치킨집의 최대 개수 M을 입력받습니다.
N, M = map(int, input().split())

# 도시 정보를 N×N 격자로 입력받습니다.
# 각 행은 공백으로 구분된 숫자들로 이루어져 있습니다.
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 좌표를 저장할 리스트를 초기화합니다.
houses = []
chicken = []

# 도시의 각 칸을 순회하면서 집(값이 1)과 치킨집(값이 2)의 좌표를 구분하여 저장합니다.
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 최소 치킨 거리를 저장할 변수, 매우 큰 값으로 초기화합니다.
min_city_distance = float('inf')

# 모든 가능한 치킨집 M개 조합을 생성합니다.
for chicken_comb in combinations(chicken, M):
    city_distance = 0  # 현재 조합에 대한 도시의 치킨 거리 합계
    # 각 집에 대해 가장 가까운 치킨집과의 거리를 구합니다.
    for hx, hy in houses:
        # 현재 집에서 선택된 치킨집들까지의 최소 거리를 구하기 위해 큰 값으로 초기화합니다.
        min_distance = float('inf')
        # 선택된 치킨집들 중에서 가장 가까운 치킨집을 찾습니다.
        for cx, cy in chicken_comb:
            # 맨해튼 거리 계산: |hx - cx| + |hy - cy|
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        # 해당 집의 최소 거리를 도시 치킨 거리에 더합니다.
        city_distance += min_distance
    # 현재 조합의 도시 치킨 거리가 지금까지의 최소값보다 작으면 업데이트합니다.
    min_city_distance = min(min_city_distance, city_distance)

# 모든 조합 중 최소 치킨 거리를 출력합니다.
print(min_city_distance)