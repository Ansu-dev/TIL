# 0번방부터 n-1번방까지 총 n개의 방이 있다. 0번 방을 제외한 모든 방은 잠겨있다.
# 우리의 목표는 모든 방에 visit하는 것이다. 하지만 잠겨있는 방은 key가 없으면 visit 할 수 없다.
# 각 방에 방문할 때, 별개의 열쇠뭉치(a set of distict keys)를 찾을 수도 있다.
# 각 열쇠에는number가 쓰여져 있고, 해당 번호에 해당하는 방을 잠금 해제할 수 있다.
# 열쇠 뭉치는 모두 가져갈 수 있고, 언제든 방문을 열기 위해 사용할 수 있다.

# 문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
# 모든 방을 visit할 수 있다면 True, 그렇지 않으면 False를 반환하라.


# n == rooms.length
# 2 <= n <= 1,000
# 0 <= rooms[i].length <= 1,000
# 1 <= sum(rooms[i].length) <= 3,000
# 0 <= rooms[i][j] < n

from collections import deque


def dfs(rooms, visited, current):
    visited[current] = True
    for next in rooms[current]:
        if not visited[next]: # O(1)
            dfs(rooms, visited, next)

def bfs(rooms, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for next in rooms[current]:
            if not visited[next]: # O(1)
                queue.append(next) # 방문하지 않은 방을 큐에 예약
                visited[next] = True

def solution(rooms):
    visited = [False] * len(rooms) # 방의 크기만큼 방문 배열을 늘린다.
    # set()을 이용 가능 -> hash set
    # {} -> dictionary
    # visited를 초기화를 시켜놓음 => [False] * len(rooms)
    # visited를 검사할 때 O(1)으로 시간 복잡도를 줄일 수 있음

    dfs(rooms, visited, 0) # dfs 0번방부터 시작
    bfs(rooms, visited, 0) # bfs 0번방부터 시작
    return all(visited) # 모든 방이 방문되어있는지 확인 (단락평가) - 첫번째 False 요소가 나올시 바로 종류



print(solution([[1],[2],[3],[]])) # True
print(solution([[1,3],[3,0,1],[2],[0]])) # False