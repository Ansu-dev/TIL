import heapq
from collections import defaultdict


# 주어진 네트워크에는 n개의 노드가 있으며, 이는 1부터 n까지 레이블이 붙어 있습니다.
# 또한 times[i] = (ui, vi, wi)리스트가 주어집니다.
# 이 때 ui노드에서 신호를 보내서 vi노드에 도달하는데 걸리는 시간을 wi라고 합니다.

# k 노드에서 신호를 보낼 때, 모든 노드에 신호가 도달하기 위한 최소 비용을 반환하시오.
# 하나의 노드라도 도달하지 못한다면 -1을 반환하시오.(한 노드에서 연결된 여러 개의 edge에 신호를 동시에 전달할 수 있습니다.)


# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 1 <= wi <= 100
# 모든 (ui, vi)쌍은 unique합니다.



def solution(times, n ,k):
    # 가중치가 있기 때문에 다익스트라 알고리즘 사용
    # k노드에서 신호를 보냄
    # n개의 레이블 4라면 1~4까지 레이블
    # 하나의 노드라도 도달하지 못한다면 -1

    # 그래프 구현
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1]))

    # 다익스트라 알고리즘
    print(graph)
    costs = {} # 딕셔너리 선언
    pq = []
    heapq.heappush(pq,(0, k)) # 시작노드

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node not in costs:
            costs[cur_node] = cur_cost # 첫방문은 그노드의 최소 비용
            for cost, next_node in graph[cur_node]: # 해당 노드에 인접 노드를 계산
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node)) # 계산된 cost와 노드를 우선순위로 넣음

    # 방문 못한 노드 찾기
    for node in range(1, n + 1): # 1 ~ n 까지 노드가 costs에 있는지 검증
        if node not in costs: # 없다면 모든 노드에 방문x
            return -1
    print(costs)
    # 최소값중에서 최대값 구하기
    # 네트워크 내에서 병렬적으로 전파. 즉, 신호는 시작 노드k에서 동시에 여러 경ㅇ로를 통해 여러 노드로 퍼져나감
    # 모든 노드에 신호가 도달하기 까지 걸리는 전체 시간은 개별 노드에 신호가 도달하는 최소 시간중에 가장 긴 시간(모든 노드가 신호를 받으려면 가장 늦게 받는 노드 시간을 기준으로 해야함)
    return max(costs.values())


# 가중치 그래프 -> 최단경로, 다익스트라
# 1. 그래프 구현 -> times의 길이만큼 O(times.length)
# 2. 다익스트라 알고리즘 O(ElogE) -> Edge의 개수만큼 push,pop을 하므로 Edge는 times의 개수 -> 최대 2^5
# 3. 방문 못한 노드 찾기 -> O(N) 노드의 개수만큼만 하면 됨
# 4. 최소값중에서 최대값 구하기 -> O(N)


print(solution([[2,1,2], [2,3,5],[2,4,1],[4,3,3]], 4, 2)) # 4
print(solution([[2,1,2], [2,3,5],[2,4,1],[4,3,3]], 4, 3)) # -1