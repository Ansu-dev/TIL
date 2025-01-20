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
