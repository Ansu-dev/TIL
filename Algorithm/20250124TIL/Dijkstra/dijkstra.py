import heap




def dijkstra(graph, start, final):
    costs = {} # cur_v의 방문 여부를 기록
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq) # 가장 작은 비용을 꺼냄
        if cur_v not in costs: # 방문 여부 판별
            costs[cur_v] = cur_cost # 비용 업데이트(우선순위큐에 의해 해당 노드가 비용이 제일 적음)
            for cost, next_v in graph[cur_v]: # 현재 노드와 연결된 노드를 확인
                next_cost = cur_cost + cost # 비용 계산
                heapq.heappush(pq, (next_cost, next_v)) # 다음 노드와, 계산한 비용을 pq에 넣어줌
    return costs[final]


graph = {
    1: [2, 4],
    2: [3, 5, 6],
    3: [6],
    4: [3, 7],
    5: [8],
    6: [5],
    7: [6, 8],
    8: []
}

print(dijkstra(graph, 1, 8))