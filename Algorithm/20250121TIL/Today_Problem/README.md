# 20250121 TIL
Today I Learned


* 항해99 1일 1코테 스터디


### ❗️ 백준 1697 - 숨바꼭질
````python
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split()) # N: 수빈이가 있는 위치, K: 동생이 있는 위치

MAX = 200000 # 점이 100,000까지이지만 2*X를 했을 경우 20만 까지 나오므로

# 가장 빠른 시간 출력 -> bfs로 각 depth의 모든 경우의 수를 탐색하면 최단 시간을 찾음
def bfs():
    # 방문 배열 만듬
    visited = [False] * (MAX + 1)
    times = [0] * (MAX + 1)

    # queue를 초기화
    queue = deque()
    queue.append(N) # 수빈이의 위치를 queue에 넣음

    visited[N] = True # 첫 노드는 방문으로 표시
    while queue: # queue가 존재할 때 까지 반복
        current = queue.popleft()

        # 현재 있는 지점이 K와 같을 경우 걸린 시간 return
        if current == K:
            return times[current] # 현재까지 걸린 시간 return

        for next in (current + 1, current - 1, current * 2): # 3가지의 모든 경우의 수를 탐색한다.
            if 0 <= next <= MAX and not visited[next]: # 범위내에 n이 존재하고, 방문하지 않았으면
                queue.append(next) # 해당 노드를 탐색해야 하므로 queue에 쌓음
                visited[next] = True # 방문 표시
                times[next] = times[current] + 1 # 현재 걸린 시간에서 + 1을 해준다.
print(bfs())

````
* 최소 시간을 구하는 문제이므로 bfs를 사용하여 해결
* 점의 범위를 특정하기위해 2*X + 1를 했을 때의 최대 범위인 200,000보다 1개 많도록 visited와 times를 구성
* queue와 visited를 통해 방문하지 않는 노드는 queue에 담고 현재 노드는 방문처리
* times의 배열에서 현재 노드로 오는 시간에 + 1을 해주어 걸리는 시간을 누적합
* 현재 노드가 K와 같아 졌을 때 함수 종료