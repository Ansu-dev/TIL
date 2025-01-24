import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = [] # 해당 빙산 위치에서 주변 바다와 접한 횟수를 저장

    while q:
        x, y = q.popleft()
        sea = 0 # 현재 노드 주변에 있는 바다(0)의 수를 세기 위한 변수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 새로운 위치가 유효한지 검색
                if not graph[nx][ny]: # 그래프의 위치가0이면 바다
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]: # 방문하지 않았고 그래프의 위치가 바다가 아니면
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0: # 주변에 바다가 1개 이상이면 seaList에 현재 위치와 바다의 수를 추가
            seaList.append((x, y, sea))
    for x, y, sea in seaList: # 빙산의 높이 감소
        graph[x][y] = max(0, graph[x][y] - sea)

    # 새로운 빙산 덩어리를 발견했음을 나타내기 위함
    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = [] # 빙산의 위치 저장
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice: # 빙산이 남아있는 동안 반복
    visited = [[0] * m for _ in range(n)] # 매년 새로운 방문 배열을 초기화
    delList = [] # 빙산이 녹아 0이된 위치를 저장할 리스트
    group = 0 # 현재 빙산 덩어리의 수를 세기 위함
    for i, j in ice: # 모든 빙산의 위치 순회(모든 빙산의 덩어리를 다 순회)
        if graph[i][j] and not visited[i][j]: # 해당 위치가 빙산이고 아직 방문하지 않았다면
            group += bfs(i, j) # 연결된 빙산 덩어리를 찾음
        if graph[i][j] == 0: # 빙산이 녹아 0이 된 위치는 삭제 리스트에 추가
            delList.append((i, j))

    if group > 1: # 빙산 덩어리가 두개 이상라면(bfs가 두번 돌았다면) 경과된 시간 출력
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList))) # ice리스트에서 delList에 있는 위치를 제거, set을 사용하여 중복을 제거
    year += 1 # 경과된 시간을 1년 증가(아직 빙산의 덩어리가 2개 이상 되지 않았으므로)

if group < 2: # python은 while문 내부의 변수도 루프 밖에서 접근이 가능
    print(0)