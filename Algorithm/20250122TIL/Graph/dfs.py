graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

visited = []

def dfs(current):
    visited.append(current) # 현재 노드를 방문 표시
    for next in graph[current]: # 현재 노드의 인접 노드를 반복문을 통해 확인
        if next not in visited: # 인접 노드가 방문 됐는지 판별
            dfs(next) # 방문되지 않았다면 재귀를 통해 해당 노드의 연결된 노드를 또 확인 -> 깊게 들어감

    return visited


print(dfs('A'))