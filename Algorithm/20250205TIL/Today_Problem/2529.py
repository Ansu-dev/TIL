import sys

input = sys.stdin.readline

# 입력 받기
k = int(input())
signs = input().split()

# 방문 여부를 확인할 리스트 (0~9)
visited = [False] * 10

# 전역 변수로 최댓값과 최솟값을 문자열로 저장 (문자열 비교 가능)
max_ans = ""
min_ans = ""

# 두 숫자 사이에 부등호 조건이 만족하는지 검사하는 함수
def check(a, b, sign):
    if sign == '<':
        return a < b
    else:  # sign == '>'
        return a > b

# 백트래킹을 이용한 DFS 함수
def dfs(depth, num_str):
    global max_ans, min_ans
    # 종료 조건: (k+1)자리 수가 완성되면
    if depth == k + 1:
        # 최초에 결과가 없으면 그대로 저장하고, 이후엔 비교해서 최솟값과 최댓값 갱신
        if not min_ans:
            min_ans = num_str
        else:
            if num_str < min_ans:
                min_ans = num_str
        if num_str > max_ans:
            max_ans = num_str
        return

    # 0부터 9까지 숫자에 대해 탐색
    for i in range(10):
        if not visited[i]:
            # 첫 숫자면 바로 진행, 아니면 이전 숫자와 부등호 조건 체크
            if depth == 0 or check(int(num_str[-1]), i, signs[depth - 1]):
                visited[i] = True
                dfs(depth + 1, num_str + str(i))
                visited[i] = False

# DFS 시작
dfs(0, "")

# 결과 출력
print(max_ans)
print(min_ans)