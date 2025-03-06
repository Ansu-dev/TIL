## 🚀 문제 개요
N = 5개의 마을이 있으며, 양방향 도로로 연결되어 있습니다.<br/>
1번 마을에서 출발하여 다른 모든 마을까지의 최단 거리를 구해야 합니다.<br/>
우선순위 큐(최소 힙) + 다익스트라 알고리즘을 사용하여 효율적으로 해결합니다.<br/>


### 그래프 구성
````python
graph = {
    1: [(1, 2), (2, 4)],
    2: [(1, 1), (3, 3), (2, 5)],
    3: [(3, 2), (1, 5)],
    4: [(2, 1), (2, 5)],
    5: [(2, 2), (1, 3), (2, 4)]
}
````

### 알고리즘 구현 및 실행 과정
✅ 1️⃣ 거리 테이블 초기화
````python
INF = float('inf')  # 무한대 값 설정
distance = [INF] * (N + 1)  # 모든 마을을 무한대로 초기화
distance[1] = 0  # 1번 마을에서 출발 → 거리 0

# [INF, 0, INF, INF, INF, INF]
````

✅ 2️⃣ 우선순위 큐 초기화
````python
pq = []
heapq.heappush(pq, (0, 1))  # (비용 0, 마을 1)

# pq = [(0, 1)]
````

✅ 3️⃣ 다익스트라 알고리즘 실행 (while loop)
````python
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
````
1. 첫번째 pq에 (0,1)을 꺼내 인접 노드를 탐색
2. cur_cost > distance[cur_v] 꺼낸 cost가 현재 cost와 차이가 없으므로 연결된 마을 탐색
3. 1번마을과 연결된 2번, 4번 마을의 비용을 갱신
4. pq에 담아 해당 마을의 연결된 마을을 또 탐색
5. 1 ~ 4번을 반복하며 queue가 빌때까지 순회

✅ 결과 출력 및 활용
````python
# distance = [INF, 0, 1, 4, 2, 3]
K = 3
print(sum(1 for i in range(2, N + 1) if distance[i] <= K))
````
* 배달 거리중에 K 이하인 마을만 카운팅