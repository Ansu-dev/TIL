import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(input().strip()) for _ in range(N)]

max_area = 1 # 최소 정사각형은 한 칸(면적 1)이다.

# 모든 가능한 시작점 (i, j)와 정사각형의 크기를 탐색
for i in range(N):
    for j in range(M):
        # 가능한 정사각형의 한 변 길이는 현재 위치에서 가능한 최대 길이(min(N-i, M-j))에 따라 정해짐
        for l in range(1, min(N - i, M - j)):
            # 정사각형의 네 꼭짓점 -> (i, j), (i, j+l), (i+l, j), (i+l, j+l)
            if grid[i][j] == grid[i][j+l] == grid[i+l][j] == grid[i+l][j+l]:
                area = (l + 1) ** 2
                if area > max_area:
                    max_area = area

print(max_area)