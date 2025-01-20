# 20250120 TIL
Today I Learned


* 항해99 1일 1코테 스터디


### ❗️ 백준 1260 - DFS와 BFS
````python
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 시작할 정점의 번호

# 1. graph 정보 입력
graph = [[False] * (N + 1) for _ in range(N + 1)]  # 2차원 배열
visited = [False] * (N + 1)


def dfs(idx):
    # 1. 노드의 자식들의 끝까지 확인 후 다음 노드
    global visited
    visited[idx] = True # 이번 노드는 방문함
    print(idx, end = ' ')
    # 재귀함수를 통해 해당 인덱스에서 방문할수 있는곳 까지 끝까지 방문
    for next in range(1, N + 1): # next라는 노드가 방문한 적이 있는지 판별
        if not visited[next] and graph[idx][next]: # 방문된적이 없고 현재 노드에서 갈수 있는 곳이라면
            dfs(next)


def bfs(idx):
    # 1. 상위 노드들 부터 먼저 다 확인
    # 2. 큐에 방문할 노드를 담아둔다.
    # 3. 방문한적이 있다면 해당 노드는 큐에 추가하지 않는다.
    global visited
    queue = deque()
    queue.append(idx) # 큐에 현재 노드를 담음
    visited[idx] = True # 현재 노드는 방문으로 표시
    while queue:
        current = queue.popleft()
        print(current, end = ' ')
        for next in range(1, N + 1):
            # 방문한적이 없고 현재 노드에 방문할수 있는 곳이 있다면 queue에 계속 담는다.
            if not visited[next] and graph[current][next]:
                visited[next] = True
                queue.append(next)



for _ in range(M):
    # 입력받은 노드를 기준으로 그래프에 표기
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

    # 2. dfs
dfs(V)
print()

# 다시 초기화
visited = [False] * (N + 1)
# 3. bfs
bfs(V)
````
1. 그래프의 노드간 간선을 True로 표시해 둔다.(1,2), (2,1)은 서로 연결된 노드 이므로 둘다 연결
2. dfs는 깊이 우선 탐색이므로 정점 노드를 기준으로 노드의 depth를 깊게 탐색하며(재귀함수) 노드이 연결을 찾는다.
3. bfs는 넓이 우선 탐색이므로 점점 노드를 기준으로 각 depth의 모든 노드를 탐색하며 노드의 연결을 queue에 쌓으며 탐색한다.


----

#### DFS
* 탐색 방식: 가능한 깊게(깊이 우선) 탐색한 후, 더 이상 갈 수 없을 때 이전 단계로 되돌아갑니다.
* 구현 방법: 주로 재귀(Recursive) 또는 명시적인 스택(Stack)을 사용하여 구현합니다.
* 방문 순서: 특정 경로를 끝까지 탐색한 후 다른 경로로 이동합니다.

````text
💡 언제 사용하는가?
경로 찾기: 두 노드 간의 모든 가능한 경로나 특정 조건을 만족하는 경로를 찾을 때 유용

사이클 탐지: 그래프에 사이클이 있는지 확인할 때 효과적

퍼즐 해결: 미로 찾기나 퍼즐 해결과 같은 문제에서 모든 가능한 상태를 탐색할 때 사용
````
* BFS에 비해 일반적으로 메모리를 덜 사용
* 재귀를 사용하여 간단하게 구현가능
* 해가 깊은 곳에 있을 때 빠르게 발견
* But, 최단 경로 보장 불가, 재귀 깊이가 너무 깊어지면 스택 오버플로우가 발생


----
#### BFS
* 탐색 방식: 현재 노드와 인접한 모든 노드를 먼저 탐색한 후, 다음 단계로 이동합니다.
* 구현 방법: 큐(Queue)를 사용하여 구현합니다.
* 방문 순서: 레벨별로 탐색하며, 가까운 노드부터 방문합니다.

````text
💡 언제 사용하는가?
최단 경로 찾기: 무가중치 그래프에서 두 노드 간의 최단 경로를 찾을 때 이상적

최소 신장 트리: BFS는 특정 조건에서 최소 신장 트리를 구성하는 데 사용

레벨 순회: 트리나 그래프의 레벨을 순서대로 탐색할 때 사용

최단 거리 계산: BFS는 모든 노드까지의 최단 거리를 계산할 때 유용

퍼즐 해결: 레벨 단위로 상태를 탐색해야 하는 퍼즐 문제에서 효과적
````
* 체계적인 탐색이 가능 - 모든 노드를 체계적으로 탐색하므로 특정 조건을 만족하는 노드를 찾을 때 유리
* 메모리 사용 예측 가능 - 최대 큐의 크기는 노드의 최대 차수에 따라 예측이 가능
* But, 그래프의 너비가 클 경우 메모리 사용량이 많아짐, 목표 노드가 깊은 곳에 있을 경우 많은 노드를 탐색하게 됨