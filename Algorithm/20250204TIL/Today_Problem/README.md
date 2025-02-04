# 20250204 TIL
Today I Learned


* 항해99 1일 1코테 스터디

### ❗️ 백준 1051 - 숫자 정사각형
````python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(input().strip()) for _ in range(N)]

max_area = 1 # 최소 정사각형은 한 칸(면적 1)이다.

# 모든 가능한 시작점 (i, j)와 정사각형의 크기를 탐색
for i in range(N):
    for j in range(M):
        # 가능한 정사각형의 한 변 길이는 현재 위치에서 가능한 최대 길이(min(N-i, M-j))에 따라 정해짐
        for l in range(1, min(N - i, M - j)): # 시작된 꼭지점 지점부터 N, M 크기를 비교해 더 작은것을 기준까지(정사각형은 네변의 길이가 모두 같기 때문에)
            # 정사각형의 네 꼭짓점 -> (i, j), (i, j+l), (i+l, j), (i+l, j+l)
            if grid[i][j] == grid[i][j+l] == grid[i+l][j] == grid[i+l][j+l]: # 4개의 꼭지점의 크기가 모두 같다면 정사각형
                # 시작점을 사용하기때문에 최소 정사각형이 1이다. 그러므로 오프셋l에서 1을 더해줘야 시작점에서 몇칸 떨어졌는지 알수 있다.
                area = (l + 1) ** 2 # 정사각형의 면적을 계산 (l+1)(l+1)
                if area > max_area:
                    max_area = area

print(max_area)
````
* 모든 위치(i, j)를 시작점으로 하여, 격자 내에서 만들 수 있는 모든 정사각형을 고려
* 각 정사각형에 대해 네 꼭짓점의 숫자가 모두 같은지 확인
* l + 1은 최소 정사각형의 한 칸 면적이 1이다. 그러므로 1 x 1 = 1, area를 계산할 때 +1을 해주어야 시작점을 포함한채 면적 계산이 된다.
* 조건에 부합하는 정사각형의 면적을 계산하고, 그중 가장 큰 면적을 max_area에 저장