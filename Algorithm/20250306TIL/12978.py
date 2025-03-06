# N: 마을의 개수, K: 음식 배달이 가능한 시간, road: [마을1, 마을2, 도로를 지나는데 걸리는 시간]
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return
# 각 도로간의 가중치가 있기 때문에 다익스트라를 사용
import heapq


# 가장치 그래프에서 시작점과 도착점이 주어졌을 때, 최단 경로를 return하는 알고리즘 -> 비가중치일 경우는 BFS
# 1번 마을은 도로가 없으므로 걸리는 시간은 0
def solution(N, road, K):
    # 방문할 수 있는 노드중에 가장 비용이 작은 곳 방문(우선순위가 높은 곳 방문) - 우선순위 큐 사용

    # 1. 우선 순위 큐에 시작노드 추가
    # 2. 우선순위가 가장 높은 노드 추출
    # 3. 방문 여부 확인
    # 4. 비용 업데이트
    # 5. 현재 노드와 연결된 노드 우선순위 큐에 추가
    # 6. 목적지에 기록된 비용 반환

    # 우선순위가 높다 = 거리가 낮다.
    # 우선순위큐에 값을 넣으면 값이 작은것부터 앞으로 정렬해준다.
    # 우선순위큐를 순회하며 비용이 3이 나올수 있는 경우를 모두 기록

    # 비 가중치 그래프 생성
    graph = {i: [] for i in range(1, N + 1)}
    for a, b, c in road: # O(N)
        graph[a].append((c, b))  # (소요 시간, 마을 번호)
        graph[b].append((c, a)) # 양방향 그래프

    INF = float('inf') # 무한대를 의미
    distance = [INF] * (N + 1)  # 모든 마을을 무한대로 초기화 5개의 마을이라면 [INF, INF, INF, INF, INF, INF] -> 1번 부터 시작하기때문
    distance[1] = 0  # 1번 마을은 거리 0으로 설정

    pq = [] # 우선순위 큐
    heapq.heappush(pq, (0, 1)) # 1번마을부터 비용0으로 시작
    while pq:
        cur_cost, cur_v = heapq.heappop(pq) # 우선순위큐에서 가장 우선순위의 비용과 마을을 꺼냄

        # 이미 더 짧은 거리로 방문한 적이 있다면 중복 방문 금지
        if cur_cost > distance[cur_v]:
            continue

        # 현재 마을에서 연결된 마을을 탐색
        for cost, next_v in graph[cur_v]:
            next_cost = cur_cost + cost # 다음 이동할 마을은 현재
            # 만약 next_cost가 기존 거리보다 짧다면 distance[next_v]를 업데이트
            if next_cost < distance[next_v]:
                distance[next_v] = next_cost
                heapq.heappush(pq, (next_cost, next_v))

    return sum(1 for d in distance if d <= K) # 5개의 마을 중에 1번 마을로부터 배달 시간이 K이하라면 sum에 그 마을의 개수를 더해준다.

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4 )) # 4