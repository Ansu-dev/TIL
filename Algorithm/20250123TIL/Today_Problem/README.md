# 20250123 TIL
Today I Learned


* 항해99 1일 1코테 스터디


### ❗️ 백준 1707 - 이분 그래프
````python3
# 런타임 에러
import sys
from collections import deque


input = sys.stdin.readline

K = int(input()) # 테스트 케이스 수
results = []

def bfs(graph, V):
    colors = [0] * (V + 1) # 색을 나타내는 배열, 0: 미방문, 1: 색1, -1: 색2

    for start in range(1, V + 1):
        if visited[start] == 0: # 아직 방문되지 않은 정점
            queue = deque(start)
            colors[start] = 1 # 첫 번째 색 할당

            while queue:
                current = queue.popleft()
                for next in graph[current]:
                    if not colors[next]:
                        colors[next] = -colors[current] # 반대 색 할당
                    elif colors[next] == colors[current]:
                        return False # 같은 색을 가진 인접 정점 발견
    return True



for _ in range(K):
    # V = 정점의 개수, E = 간선의 개수
    V, E = map(int, input().split())
    # 그래프 초기화 및 입력 받기
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split()) # 인접한 각 정점의 번호
        graph[u].append(v)
        graph[v].append(u)

    # 이분 그래프 판별
    if bfs(graph, V):
        results.append("YES")
    else:
        results.append("NO")

print('\n'.join(results))
````