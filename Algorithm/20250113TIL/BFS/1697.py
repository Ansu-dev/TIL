import sys
from collections import deque

input =  sys.stdin.readline

N, K = map(int, input().split())

MAX = 200000 # 각점의 최대는 10만이지만 순간이동시에 20만이 되기때문에


# N = 5가 K = 17이 되려면 3가지 방법을 계속해서 해보면서 정답을 찾음
# N - 1(1초 뒤로 걷기), N + 1(1초 앞으로 걷기), 2 * N(1초 순간이동)
# 5 -> 4, 6, 10
    # 4 -> 3, 5, 8
        # 3 -> 2, 4, 6
            # 2 -> 1, 3, 4
            # 4 -> 3, 5, 8
            # 6 -> 5, 7, 12
        # 5 -> 4, 6, 10
            # 4 -> 3, 5, 8
            # 6 -> 5, 7, 12
            # 10 -> 9, 11, 20
        # 8 -> 7, 9, 16
            # 7 -> 6, 8, 14
            # 9 -> 8, 10, 18
            # 16 -> 15, 17, 32 # 정답
    # 6 -> 5, 7, 12
        # 5 -> 4, 6, 10
        # 7 -> 6, 8, 14
        # 12 -> 11, 13, 24
    # 10 -> 9, 11, 20
        # 9 -> 9, 10, 18
        # 11 -> 10, 12, 22
        # 20 -> 19, 21, 40

# 이 그래프를 어떻게 옮기며
# bfs의 식을 어떻게 짤까?
# root tree = 5
# target tree = 17

def bfs(N, K):
    # 방문 여부 및 시간을 저장할 리스트 초기화
    visited = [False] * (MAX + 1)
    time = [0] * ( MAX + 1)

    # BFS를 위한 큐 초기화
    queue = deque()
    queue.append(N) # 처음 노드는 방문을 하니 큐에 담아둠
    visited[N] = True # N의 좌표는 방문했으니 방문 체크

    while queue: # queue가 존재할 때까지 반복
        current = queue.popleft() # queue의 첫번째를 현재로 두고 비교

        # 목표에 도달하면 결과 반환
        if current == K:
            return time[current]

        # 가능한 3가지 연산을 수행
        # 여기서 각 노드를 탐색
        for next_position in (current - 1, current + 1, 2 * current):
            # 유효한 위치인지 확인
            if 0 <= next_position <= MAX and not visited[next_position]:
                queue.append(next_position) #
                visited[next_position] = True # 방문 표시
                time[next_position] = time[current] + 1 # 현재 시간 배열에서 1을 더해준채 그 위치에 시간 저장

print(bfs(N, K))
