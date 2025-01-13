import sys
from collections import deque

input =  sys.stdin.readline

M, N = map(int, input().split())



# 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수
# 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 저장된 날 때부터 모든 토마토가 익어있는 상태이면 0, 토마토가 모두 익지는 못하는 상황이면 -1

def bfs(queue, grid, M, N):
    # 이동할 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    days = -1  # 시작은 -1로 설정하여 첫날 0으로 맞춤

    while queue:
        days += 1
        for _ in range(len(queue)): # queue만큼 반복문
            x, y = queue.popleft() # 익은 토마토의 위치를 꺼냄
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < N and 0 <= new_y < M and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y))

    return days


def main():
    grid = []
    queue = deque()
    for i in range(N):
        # 각 행을 입력받아 정수 리스트로 변환
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(M):
            if row[j] == 1:
                queue.append((i, j))  # 익은 토마토의 위치를 queue에 넣음

    # bfs를 통해 모든 토마토를 익히기
    days = bfs(queue, grid, M, N)

    # 모든 토마토가 익어있지 않을 경우 -1 출력
    for row in grid:
        if 0 in row:
            print(-1)
            return

    # 모든 토마토가 익어있지 않을 경우는 제외(문제에서 적어도1개는 익었다고 가정)
    # 모든 토마토가 익어있을 경우는 while이 1번 돈뒤 모든 큐가 사라지니 days는 자동으로 0
    print("days: ", days)

main()