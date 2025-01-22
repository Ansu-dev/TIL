from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

def bfs(graph, start):
    visited = [start] # 맨처음 노드는 방문으로 취급
    queue = deque(start) # 처음 노드를 큐에 넣고 시작
    while queue: # queue가 존재 할 때 까지 순회
        current = queue.popleft() # FIFO에 의해 현재 탐색할 노드를 꺼내옴
        for next in graph[current]: # 현재 노드에서 인접 노드가 있는지 판별
            if next not in visited: # 인접 노드가 방문한적 있는지 판별
                visited.append(next)
                queue.append(next)
    return visited


print(bfs(graph, 'A'))