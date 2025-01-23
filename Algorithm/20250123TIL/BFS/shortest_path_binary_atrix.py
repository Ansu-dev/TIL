# n x n binary matrix의 grid가 주어졌을 때, 출발지에서 목적지 까지 도착하는 가장 빠른
# 경로의 길이를 반환하시오. 만약 경로가 업삳면 -1을 반환하시오.

# 출발지: top-left cell
# 목적지: bottom-right cell

# 제한사항
# 값이 0인 cell만 지나갈 수 있다.
# cell까리는 8가지 방향으로 연결되어 있다.(edge와 corner 방향으로 총 8가지이다.)
# 연결된 cell을 통해서만 지나갈 수 있다.

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from collections import deque

grid1 = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]

grid2 = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, visited):
    queue = deque([(0, 0)])
    visited[0][0] = True # 첫번째 노드는 방문
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 1:
            return -1



def solution(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    count = bfs(grid, visited)
    return count


print(solution(grid1)) # 4
print(solution(grid2)) #