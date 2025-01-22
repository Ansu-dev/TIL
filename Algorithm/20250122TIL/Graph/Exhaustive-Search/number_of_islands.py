from collections import deque

# grid는 "1"(land)과 "0"(watter)으로 이루어진 지돌르 표현하는 m x n 이차원배열이다. 이 지도에 표시된 섬들의 총 개수를 반환하시오.
# 섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러쌓여있는 것을 말한다. 또한, grid의 네개의 가장자리는 모두 물로 둘러쌓여있다고 가정하고 문제를 해결하라
#
# 제약 조건
# m == grid.length
# n == grid[i].length
# 1 <= m, n<= 300 => 10^5 승이므로 O(n^2)으로는 풀 수 없다.
# grid[i][j] is '0' or '1'

# 제약조건을 확인하고 어떤 알고리즘을 사용할 지 파악해야함
# O(NlogN)이나,O(N)으로 풀어야함

grid1 = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]

grid2 = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]


MAX = 301

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 그래프의 연결 요소 찾기 BFS/DFS 어떤것을 사용해도 무방 -> 탐색하는 순서만 다를뿐 결국 모든 노드를 탐색해야함
def solution(grid):
    # 직관으로 풀수 있는것을 -> 확장
    # 완전 탐색으로 시작 -> 확장 -> 시간복잡도를 낮추기위해 -> 다른 알고리즘 선택
    visited = [[False] * MAX for _ in range(MAX)]
    count = 0

    def bfs(i, j):  # bfs는 파라미터가 많아도 1번 호출 되니 메모리상 문제가 없음
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            # 상,하,좌,우의 노드를 방문하며 방문이 되어있는지 판별
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y  # 새로운 x
                # 범위내에 포함되어있고, grid가 1이고 방문하지 않았다면
                if 0 <= new_dx <= len(grid) - 1 and 0 <= new_dy <= len(grid[0]) - 1 and grid[new_dx][
                    new_dy] == '1' and not visited[new_dx][new_dy]:
                    queue.append((new_dx, new_dy))
                    visited[new_dx][new_dy] = True
        return

    def dfs(i, j):
        visited[i][j] = True
        for dx, dy in directions:
            new_dx, new_dy = dx + i, dy + j
            if 0 <= new_dx <= len(grid) - 1 and 0 <= new_dy <= len(grid[0]) - 1 and grid[new_dx][
                new_dy] == '1' and not visited[new_dx][new_dy]:
                dfs(new_dx, new_dy)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            # bfs를 들어가기전에 노드가 1이라면 새로운 섬이므로 count를 한 후 bfs 실행
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                bfs(i, j)
                # dfs(i, j)



    return count





print('grid1 : ',solution(grid1)) # 1
print('grid2 : ',solution(grid2)) # 3