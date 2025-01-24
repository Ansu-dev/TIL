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

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

def bfs(grid, visited):
    path_length = -1

    queue = deque([(0, 0, 1)])
    visited[0][0] = True # 첫번째 노드는 방문
    while queue:
        x, y, l = queue.popleft()
        # 목적지에 도착했을 때 그때의 path_lenth에 저장하면 됨
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            path_length = l # 가장 빨리 끝나는 length가 path_length에 담김
            break

        for dx,dy in directions:
            new_dx, new_dy = dx + x, dy + y
            if 0 <= new_dx < len(grid) and 0 <= new_dy < len(grid[0]) and not visited[new_dx][new_dy] and grid[new_dx][new_dy] == 0:
                queue.append((new_dx, new_dy, l + 1)) # 길이 정보도 함께 넣어 준다(최단 경로를 구하기 위해서)
                visited[new_dx][new_dy] = True

    return path_length



def solution(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    if grid[0][0] == 1 or gird[len(grid) - 1][len(grid[0] - 1)] == 1: # 시작이1이거나 끝지점이 1인 경우는 -1 반환
        return -1
    return bfs(grid, visited)


print(solution(grid1)) # 4
print(solution(grid2)) #