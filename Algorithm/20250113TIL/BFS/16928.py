import sys
from collections import deque

input =  sys.stdin.readline

N, M = map(int, input().split())

def bfs(boards):
    # 방문 배열
    visited = [False] * 101
    queue = deque()

    # 시작점:1 번 칸, 굴림 횟수 0회
    queue.append((1, 0))
    visited[1] = True

    while queue:
        # queue에 쌓인 현재 위치와 주사위 굴림 횟수를 가져옴
        current, rolls = queue.popleft()

        # 현재 위치가 100이면 더 주사위를 굴릴 필요없음
        if current == 100:
            return rolls

        # 주사위를 굴려 1~6 이동
        for i in range(1, 7): # 1 ~ 6까지
            next_position = current + i # 현재 위치에서 주사위 숫자만큼 이동
            if next_position > 100: # 만약 굴린 주사위가 100을 초과하면 이동 불가
                continue

            # 사다리나 뱀이 있다면 이동 후 도착지로 설정




    return


def main():
    boards = [i for i in range(101)]  # 100개의 격자 그리드가 필요, 0번 인덱스를 사용하지 않음

    # 사다리 정보
    for _ in range(M):
        x, y = map(int, input().split())
        boards[x] = y

    # 뱀 정보 입력
    for _ in range(N):
        u, v = map(int, input().split())
        boards[u] = v

    print(bfs(boards))

main()